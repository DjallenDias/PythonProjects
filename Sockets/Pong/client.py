import pygame
import socket
import threading
import time
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("localhost", 8081))

def recieve():
    global infos
    while thread_run:
        data = server.recv(1024).decode()
        try:
            infos = json.loads(data)
            print(infos)
        except json.decoder.JSONDecodeError: pass

thread_run = True
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

pygame.init()
screen = pygame.display.set_mode((660, 400))
pygame.display.set_caption("client")
font = pygame.font.Font(None, 28)
clock = pygame.time.Clock()

ball_pos = pygame.Vector2(0,0)
left_rect_pos = pygame.Rect(0,0,10,80)
right_rect_pos = pygame.Rect(0,0,10,80)


def show_points(blue_points, red_points):
    ren_txt_blue = font.render(f"{blue_points}", True, "blue")
    ren_txt_bar = font.render("|", True, "white")
    ren_txt_red = font.render(f"{red_points}", True, "red")
    screen.blit(ren_txt_blue, (screen.get_width()/2-30,10))
    screen.blit(ren_txt_bar, (screen.get_width()/2,10))
    screen.blit(ren_txt_red, (screen.get_width()/2+20,10))

running = True
time.sleep(0.5)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            thread_run = False
            running = False

    ball_pos.x = infos["ball_pos"][0]
    ball_pos.y = infos["ball_pos"][1]

    left_rect_pos.x = infos["blue_rect_pos"][0]
    left_rect_pos.y = infos["blue_rect_pos"][1]

    right_rect_pos.x = infos["red_rect_pos"][0]
    right_rect_pos.y = infos["red_rect_pos"][1]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        server.send(str(pygame.K_w).encode())
    elif keys[pygame.K_s]:
        server.send(str(pygame.K_s).encode())

    screen.fill("black")

    show_points(infos["blue_points"], infos["red_points"])

    pygame.draw.circle(screen, "white", ball_pos, 10)
    pygame.draw.rect(screen, "blue", left_rect_pos)
    pygame.draw.rect(screen, "red", right_rect_pos)

    pygame.display.flip()

pygame.quit()