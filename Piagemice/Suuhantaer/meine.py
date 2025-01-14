from random import randint
import pygame
pygame.init()
pygame.init()
pygame.mixer.init()
pygame.font.init()
font = pygame.font.Font(None, 40)

WIDTH = 1200
HEIGHT = 600
HWITE = (255, 255, 255)
BLACH = (0, 0, 0)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suuhantaer")
bg = pygame.transform.scale(pygame.image.load('./Suuhantaer/tloes.png'), (WIDTH, HEIGHT))
playinhu = pygame.mixer.music.load('./Suuhantaer/Hrimnir.ogg')
pygame.mixer.music.play()

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, palehin_image, palehin_har, palehin_jel, palehin_w, palehin_h, palehin_sweh):
        super().__init__()
        self.palehin_h = palehin_h
        self.palehin_w = palehin_w
        self.image = pygame.transform.scale(pygame.image.load(palehin_image), (palehin_w, palehin_h))
        self.speed = palehin_sweh
        self.rect = self.image.get_rect()
        self.rect.x = palehin_har
        self.rect.y = palehin_jel
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Palehin(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < 1150:
            self.rect.x += self.speed

    def sahurdier(self):
        sahurdhe = Sahurd('./Suuhantaer/sahurd.png', self.rect.x, self.rect.centery, 15, 15, 20)
        sahurdaes.add(sahurdhe)

score = 0
lost = 0
class Kurhen(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= HEIGHT:
            self.rect.x = randint(80, HEIGHT - 80)
            self.rect.y = 0
            lost = lost + 1

class Sahurd(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


palehin = Palehin('./Suuhantaer/gravienker.png', 100, HEIGHT - 100, 75, 75, 5)

kurhentie = pygame.sprite.Group()
for i in range(1, 5):
    kurhent = Kurhen('./Suuhantaer/kurhen.png', randint(
        80, WIDTH - 80), -40, 50, 80, randint(1, 3))
    kurhentie.add(kurhent)

sahurdaes = pygame.sprite.Group()

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                
    if finish != True:
        window.fill((0, 0, 0))
        window.blit(bg, (0, 0))
        text_lose = font.render("пропустив лошара:" + str(lost), 0, HWITE)
        text = font.render("настріляв:" + str(score), 0, HWITE)
        window.blit(text_lose, (10, 70))
        window.blit(text, (10, 30))

        palehin.reset()
        palehin.update()

        kurhentie.draw(window)
        kurhentie.update()


    pygame.display.update()
    clock.tick(60)

pygame.quit()