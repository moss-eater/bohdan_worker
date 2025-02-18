import pygame
pygame.init()

BLACH = (0, 0, 0)
WIDTH = 800
HEIGHT = 600

font1 = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dung Crawl")



game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if finish != True:
        window.fill(BLACH)
        