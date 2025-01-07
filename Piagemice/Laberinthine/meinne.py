import pygame
import pygame.mixer
pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinthihe")
bg = pygame.transform.scale(pygame.image.load('./Laberinthihe/tloes.png'), (WIDTH, HEIGHT))
playinhu = pygame.mixer.music.load('./Laberinthihe/Boiling-Mine-OST-Stone-Story-RPG.ogg')
pygame.mixer.music.play()

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

class Palehin(GameSprite):
    def __init__(self, palehin_image, palehin_har, palehin_jel, palehin_sweh):
        super().__init__(palehin_image, palehin_har, palehin_jel, palehin_sweh)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < 1150:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 550:
            self.rect.y += self.speed

class Gigurandes(GameSprite):
    def __init__(self, palehin_image, palehin_har, palehin_jel, palehin_sweh):
        super().__init__(palehin_image, palehin_har, palehin_jel, palehin_sweh)

    direction1 = 'left'
    direction = 'left'

    def update_1(self):
        if self.rect.x <= (WIDTH - 300):
            self.direction1 = 'right'
        if self.rect.x >= (WIDTH - 100):
            self.direction1 = 'left'

        if self.direction1 == 'left':
            self.rect.x -= self.speed
        if self.direction1 == 'right':
            self.rect.x += self.speed

    def update_2(self):
        if self.rect.x <= (WIDTH - 1050):
            self.direction = 'right'
        if self.rect.x >= (WIDTH - 650):
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

palehin = Palehin('./Laberinthihe/gravienker.png', 100, HEIGHT - 150, 4)
gigurandes_ih = Gigurandes('./Laberinthihe/giaghenti.png', WIDTH - 170, 300, 3)
gigurandes_ej = Gigurandes('./Laberinthihe/giaghenti.png', WIDTH - 1000, 100, 2)
sahurdaes = GameSprite('./Laberinthihe/der_prizen.png', WIDTH - 170, HEIGHT - 170, 0)


game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if finish != True:
        window.fill((0, 0, 0))
        window.blit(bg, (0, 0))

        palehin.reset()
        palehin.update()

        gigurandes_ih.reset()
        gigurandes_ih.update_1()

        gigurandes_ej.reset()
        gigurandes_ej.update_2()

        sahurdaes.reset()

        #when palehin toucher sahurdaes do pygame.mixer.music.stop(playinhu)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
