import pygame
import socket
import threading
import random
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8081))
server.listen()

conn, addr = server.accept()

data = ""
def recieve():
    global data, thread_run, running
    while thread_run:
        try:
            data = conn.recv(1024*5).decode()
        except ConnectionResetError:
            thread_run = False
            running = False


def send(ball_pos, left_rect_pos, right_rect_pos):
    global thread_run, running
    infos = str(left_rect_pos) + str(right_rect_pos) + str(ball_pos)
    try:
        conn.send(infos.encode())
    except BrokenPipeError:
        thread_run = False
        running = False

screen = pygame.display.set_mode((660, 400))
pygame.display.set_caption("server")

ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
left_rect_pos = pygame.Rect(10,10,10,80)
right_rect_pos = pygame.Rect(screen.get_width()-20,10,10,80)
send((ball_pos.x, ball_pos.y),
        (left_rect_pos.x, left_rect_pos.y),
        (right_rect_pos.x, right_rect_pos.y))

running = True
thread_run = True

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

clock = pygame.time.Clock()

ball_up = random.choice([True, False])
ball_left = random.choice([True, False])

time.sleep(1)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            thread_run = False
            running = False

    screen.fill("black")
    ball = pygame.draw.circle(screen, "white", ball_pos, 10)
    left_rect = pygame.draw.rect(screen, "white", left_rect_pos)
    right_rect = pygame.draw.rect(screen, "white", right_rect_pos)

    send((ball_pos.x, ball_pos.y),
        (left_rect_pos.x, left_rect_pos.y),
        (right_rect_pos.x, right_rect_pos.y))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: left_rect_pos.y -= 6
    elif keys[pygame.K_s]: left_rect_pos.y += 6

    if data.isdecimal():
        if int(data) == pygame.K_w:
            right_rect_pos.y -= 6
        elif int(data) == pygame.K_s:
            right_rect_pos.y += 6
        data = ""

    if ball_up:
        ball_pos.y -= 1
    else:
        ball_pos.y += 1

    if ball_left:
        ball_pos.x -= 1
    else:
        ball_pos.x += 1

    if ball.y <= 0:
        ball_up = False

    if ball.y >= screen.get_height()-10:
        ball_up = True

    if ball.colliderect(left_rect):
        ball_left = False

    if ball.colliderect(right_rect):
        ball_left = True

    pygame.display.flip()