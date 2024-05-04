import pygame
import random
import socket
import time
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8081))
server.listen()
conn, addr = server.accept()

pygame.init()
screen = pygame.display.set_mode((660, 400))
pygame.display.set_caption("server")
font = pygame.font.Font(None, 28)
clock = pygame.time.Clock()

ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
left_rect_pos = pygame.Rect(10,10,10,80)
right_rect_pos = pygame.Rect(screen.get_width()-20,10,10,80)

running = True
ball_up = random.choice([True, False])
ball_left = random.choice([True, False])

blue_points = 0
red_points = 0

def ver_ball_collision(left_rect, right_rect):
    global ball_up, ball_left, ball_pos
    if ball.y <= 0:
        ball_up = False
    if ball.y >= screen.get_height()-20:
        ball_up = True

    if ball.colliderect(left_rect):
        ball_left = False

    if ball.colliderect(right_rect):
        ball_left = True

def move_ball():
    global ball_up, ball_left, ball_pos
    if ball_up:
        ball_pos.y -= 4
    else:
        ball_pos.y += 4

    if ball_left:
        ball_pos.x -= 4
    else:
        ball_pos.x += 4

def show_points(blue_points, red_points):
    ren_txt_blue = font.render(f"{blue_points}", True, "blue")
    ren_txt_bar = font.render("|", True, "white")
    ren_txt_red = font.render(f"{red_points}", True, "red")
    screen.blit(ren_txt_blue, (screen.get_width()/2-30,10))
    screen.blit(ren_txt_bar, (screen.get_width()/2,10))
    screen.blit(ren_txt_red, (screen.get_width()/2+20,10))

def reset_game():
    global ball_pos, ball_up, ball_left
    ball_up = random.choice([True, False])
    ball_left = random.choice([True, False])
    ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

def send_game_infos(ball_pos, blue_rect_pos, red_rect_pos, blue_points, red_points):
    infos = dict()
    infos["ball_pos"] = (ball_pos.x, ball_pos.y)
    infos["blue_rect_pos"] = (blue_rect_pos.x, blue_rect_pos.y)
    infos["red_rect_pos"] = (red_rect_pos.x, red_rect_pos.y)
    infos["blue_points"] = blue_points
    infos["red_points"] = red_points
    json_infos = json.dumps(infos)
    conn.send(json_infos.encode())
    print(json_infos)

def recieve_keys():
    global data, thread_run, running
    data = ""
    while thread_run:
        try:
            data = conn.recv(1024).decode()
        except ConnectionResetError:
            thread_run = False
            running = False


thread_run = True
recieve_thread = threading.Thread(target=recieve_keys)
recieve_thread.start()

send_game_infos(ball_pos, left_rect_pos, right_rect_pos, blue_points, red_points)

time.sleep(0.5)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            thread_run = False
            running = False

    screen.fill("black")
    ball = pygame.draw.circle(screen, "white", ball_pos, 10)
    left_rect = pygame.draw.rect(screen, "blue", left_rect_pos)
    right_rect = pygame.draw.rect(screen, "red", right_rect_pos)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: left_rect_pos.y -= 6
    elif keys[pygame.K_s]: left_rect_pos.y += 6

    if data.isdecimal():
        if int(data) == pygame.K_w:
            right_rect_pos.y -= 6
        elif int(data) == pygame.K_s:
            right_rect_pos.y += 6
        data = ""

    move_ball()
    show_points(blue_points, red_points)
    ver_ball_collision(left_rect, right_rect)

    if ball.x <= 0:
        reset_game()
        red_points += 1
    if ball.x >= screen.get_width():
        reset_game()
        blue_points += 1

    send_game_infos(ball_pos, left_rect_pos, right_rect_pos, blue_points, red_points)

    pygame.display.flip()

pygame.quit()