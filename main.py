import pygame
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Collision Detection")
clock=pygame.time.Clock()


BLUE=(0,0,255)
RED=(255,0,0)
WHITE=(255,255,255)




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect(center=(100,100))
        self.speed=5
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if keys[pygame.K_UP]:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speed
        self.rect.clamp_ip(screen.get_rect())
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect=self.image.get_rect(center=(700,300))
player=Player()
enemy=Enemy()
all_sprites=pygame.sprite.Group()
enemy_sprite=pygame.sprite.Group()


all_sprites.add(player,enemy)
enemy_sprite.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)