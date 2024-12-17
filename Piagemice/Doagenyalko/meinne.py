import pygame
import random

pygame.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doagenyalko")
bg = pygame.transform.scale(pygame.image.load('le_fieldince.png'), (WIDTH, HEIGHT))

clock = pygame.time.Clock()

def coordsx():
    liste = [2, 3, 4, 6, 12]
    dili = random.choice(liste)
    x = WIDTH/dili
    return x

def coordsy():
    liste = [2, 3, 6]
    dili = random.choice(liste)
    y = HEIGHT/dili
    return y

x1 = coordsx()
y1 = coordsy()
x2 = coordsx()
y2 = coordsy()

speed = 5

first_player = pygame.transform.scale(pygame.image.load('player_1.png'), (40, 40))
second_player = pygame.transform.scale(pygame.image.load('player_2.png'), (40, 40))

game_over = False
while not game_over:
    window.fill((0, 0, 0))

    window.blit(bg, (0, 0))
    window.blit(first_player, (x1, y1))
    window.blit(second_player, (x2, y2))

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_LEFT] and x1 > 5:
        x1 -= speed
    if key_pressed[pygame.K_RIGHT] and x1 < 1150:
        x1 += speed
    if key_pressed[pygame.K_UP] and y1 > 5:
        y1 -= speed
    if key_pressed[pygame.K_DOWN] and y1 < 550:
        y1 += speed

    if key_pressed[pygame.K_a] and x2 > 5:
        x2 -= speed
    if key_pressed[pygame.K_d] and x2 < 1150:
        x2 += speed
    if key_pressed[pygame.K_w] and y2 > 5:
        y2 -= speed
    if key_pressed[pygame.K_s] and y2 < 550:
        y2 += speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
