import pygame
import pygame.mixer
pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH = 1200
HEIGHT = 600
INCAWEHA = (180, 0, 0)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinthihe")
bg = pygame.transform.scale(pygame.image.load('tloes.png'), (WIDTH, HEIGHT))
playinhu = pygame.mixer.music.load('Boiling-Mine-OST-Stone-Story-RPG.ogg')
pygame.mixer.music.play()

gay = pygame.mixer.Sound("gay.ogg")
straight = pygame.mixer.Sound("straight.ogg")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 35)
winesse = font.render('You gained back thine tools', True, (INCAWEHA))
loisien = font.render('You lost to the guardians of stolen', True, (INCAWEHA))


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

class Ta(pygame.sprite.Sprite):
    def __init__(self, clr1, clr2, clr3, ta_har, ta_jel, ta_w, ta_h):
        super().__init__()
        self.colour1 = clr1
        self.colour2 = clr2
        self.colour3 = clr3
        self.width = ta_w
        self.height = ta_h

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((clr1, clr2, clr3))

        self.rect = self.image.get_rect()
        self.rect.x = ta_har
        self.rect.y = ta_jel

    def draw_ta(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

palehin = Palehin('gravienker.png', 100, HEIGHT - 150, 4)
gigurandes_ih = Gigurandes('giaghenti.png', WIDTH - 170, 300, 3)
gigurandes_ej = Gigurandes('giaghenti.png', WIDTH - 1000, 100, 2)
sahurdaes = GameSprite('der_prizen.png', WIDTH - 170, HEIGHT - 170, 0)

ta1 = Ta(154, 140, 0, 200, 90, 450, 10)
ta2 = Ta(154, 140, 0, 0, 510, 265, 10)
ta3 = Ta(154, 140, 0, 0, 445, 205, 10)
ta4 = Ta(154, 140, 0, 200, 200, 10, 255)
ta5 = Ta(154, 140, 0, 265, 200, 10, 320)

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

        ta1.draw_ta()
        ta2.draw_ta()
        ta3.draw_ta()
        ta4.draw_ta()
        ta5.draw_ta()

        if pygame.sprite.collide_rect(palehin, gigurandes_ih) or pygame.sprite.collide_rect(palehin, gigurandes_ej) or pygame.sprite.collide_rect(palehin, ta1):
            finish = True
            window.blit(loisien, (200, 200))
            gay.play()

        if pygame.sprite.collide_rect(palehin, sahurdaes):
            finish = True
            window.blit(winesse, (200, 200))
            straight.play()    

        #when palehin toucher sahurdaes do pygame.mixer.music.stop(playinhu)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
