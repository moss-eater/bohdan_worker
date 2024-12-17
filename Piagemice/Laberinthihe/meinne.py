import pygame
import pygame.mixer
pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinthihe")
bg = pygame.transform.scale(pygame.image.load('./Laberinthihe/tloes.png'), (WIDTH, HEIGHT))

clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, palehin_image, palehin_har, palehin_jel, palehin_sweh):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(palehin_image), (50, 50))
        self.speed = palehin_sweh
        self.rect = self.image.get_rect()
        self.rect.x = palehin_har
        self.rect.y = palehin_jel
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


palehin = GameSprite('./Laberinthihe/gravienker.png', 100, HEIGHT - 150, 4)
gigurandes_iho = GameSprite('./Laberinthihe/giaghenti.png', WIDTH - 170, 300, 2)
gigurandes_ej = GameSprite('./Laberinthihe/giaghenti.png', WIDTH - 1000, 100, 3)
sahurdaes = GameSprite('./Laberinthihe/der_prizen.png', WIDTH - 170, HEIGHT - 170, 0)


game_over = False
while not game_over:
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))

    palehin.reset()
    gigurandes_iho.reset()
    gigurandes_ej.reset()
    sahurdaes.reset()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
