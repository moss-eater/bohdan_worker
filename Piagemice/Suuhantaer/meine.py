import pygame
pygame.init()
pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suuhantaer")
bg = pygame.transform.scale(pygame.image.load('tloes.png'), (WIDTH, HEIGHT))
playinhu = pygame.mixer.music.load('Hrimnir.ogg')
pygame.mixer.music.play()

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, palehin_image, palehin_har, palehin_jel, palehin_sweh):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(palehin_image), (100, 100))
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

palehin = Palehin('gravienker.png', 100, HEIGHT - 100, 5)

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

    pygame.display.update()
    clock.tick(60)

pygame.quit()