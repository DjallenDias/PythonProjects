import pygame
import socket
import threading
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8081))

data = ""
def recieve():
    global data, left_rect_y, right_rect_y, ball_x, ball_y
    while thread_run:
        data = client.recv(1024*5).decode()
        data = data.replace("(", " ").replace(")", " ")
        data = data.split("  ")
        # print(data)
        left_rect_y = int(data[0].replace(" ", "").split(",")[1])
        right_rect_y = int(data[1].replace(" ", "").split(",")[1])
        ball_x = float(data[2].replace(" ", "").split(",")[0])
        ball_y = float(data[2].replace(" ", "").split(",")[1])

screen = pygame.display.set_mode((660, 400))
pygame.display.set_caption("client")

ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
left_rect_pos = pygame.Rect(10,10,10,80)
right_rect_pos = pygame.Rect(screen.get_width()-20,10,10,80)

thread_run = True
running = True

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

clock = pygame.time.Clock()

time.sleep(1)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            thread_run = False
            running = False

    screen.fill("black")
    pygame.draw.circle(screen, "white", ball_pos, 10)
    pygame.draw.rect(screen, "white", left_rect_pos)
    pygame.draw.rect(screen, "white", right_rect_pos)

    left_rect_pos.y = left_rect_y
    right_rect_pos.y = right_rect_y
    ball_pos.x = ball_x
    ball_pos.y = ball_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        client.send(str(pygame.K_w).encode())
    elif keys[pygame.K_s]:
        client.send(str(pygame.K_s).encode())

    pygame.display.flip()