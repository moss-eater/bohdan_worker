from random import randint
import pygame
import time
pygame.init()
pygame.mixer.init()
pygame.font.init()

from time import time as timer
WIDTH = 1000
HEIGHT = 650
HWITE = (255, 255, 255)
BLACH = (0, 0, 0)
REDD = (230, 0, 0)

font = pygame.font.Font(None, 45)
font1 = pygame.font.Font(None, 25)
win = font.render("ПєРєМОГА", True, REDD)
loss = font.render("Тебе з'їли", True, REDD)


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suuhantaer")
bg = pygame.transform.scale(pygame.image.load('tloes.png'), (WIDTH, HEIGHT))
playinhu = pygame.mixer.music.load('Batalenh.ogg')
pygame.mixer.music.play()
sahurdin_sund = pygame.mixer.Sound('sahursunt.ogg')

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

    def sahurdiner(self):
        sahurdhe = Sahurd('sahurd.png', self.rect.x, self.rect.centery, 50, 60, 20)
        sahurdaes.add(sahurdhe)

score = 0
goooooooooooooooooooool = 20
lost = 0
max_lost = 4
liite = 2
class Kurhen(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= HEIGHT:
            self.rect.x = randint(80, HEIGHT - 80)
            self.rect.y = 0
            lost = lost + 1

class Sarja(GameSprite):
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


palehin = Palehin('gravienker.png', WIDTH/2, HEIGHT - 100, 75, 75, 6)

kurhentie = pygame.sprite.Group()
for i in range(1, 4):
    kurhent = Kurhen('kurhen.png', randint(80, WIDTH - 80), -40, 50, 80, 2)
    kurhentie.add(kurhent)

sarjie = pygame.sprite.Group()
for i in range(1, 2):
    sarjat = Sarja('sarja.png', randint(80, WIDTH - 80), -40, 90, 90, randint(1, 4))
    sarjie.add(sarjat)

giaghenti = Kurhen('giaghenti.png', randint(80, WIDTH - 80), -40, 160, 160, 1)

sahurdaes = pygame.sprite.Group()

rel_time = False
num_sahurdua = 0

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if num_sahurdua < 6 and rel_time == False:
                    num_sahurdua += 1
                    sahurdin_sund.play()
                    palehin.sahurdiner()
            if num_sahurdua >= 6 and rel_time == False:
                last_time = timer()
                rel_time = True


    if finish != True:
        window.fill(HWITE)
        window.blit(bg, (0, 0))

        text_lose = font.render("пропустив лобуряка:" + str(lost), 0, HWITE)
        window.blit(text_lose, (10, 70))

        text = font.render("настріляв:" + str(score), 0, HWITE)
        window.blit(text, (10, 30))

        palehin.reset()
        palehin.update()

        kurhentie.draw(window)
        kurhentie.update()
        sarjie.draw(window)
        sarjie.update()


        giaghenti.update()
        if liite > 0:
            giaghenti.reset()

        colligion = pygame.sprite.spritecollide(giaghenti, sahurdaes, True)
        if colligion:
            score +=1
            liite -= 1
            print(liite)
            if liite < 0:
                giaghenti.kill()

        sahurdaes.draw(window)
        sahurdaes.update()

        if rel_time == False:
            now_time = timer()

            if now_time - last_time < 3:
                reload = font1.render('шукаю нові мечі...')
                window.blit(reload, (0, 0))
            else:
                num_sahurdua = 0
                rel_time = False


        collizion = pygame.sprite.groupcollide(kurhentie, sahurdaes, True, True)
        for z in collizion:
            score += 1
            kurhent = Kurhen('kurhen.png', randint(80, WIDTH - 80), -40, 50, 80, randint(1, 2))
            kurhentie.add(kurhent)

        collition = pygame.sprite.groupcollide(sarjie, sahurdaes, True, True)
        for t in collition:
            score += 2
            sarjat = Sarja('sarja.png', randint(80, WIDTH - 80), -40, 90, 90, randint(1, 4))
            sarjie.add(sarjat)

        if pygame.sprite.spritecollide(palehin, kurhentie, False) or lost > max_lost:
            finish = True
            window.fill(HWITE)
            window.blit(loss, (200, 200))

        if score >= goooooooooooooooooooool:
            finish = True
            window.fill(HWITE)
            window.blit(win, (200, 200))

    pygame.display.update()
    clock.tick(60)

pygame.quit()