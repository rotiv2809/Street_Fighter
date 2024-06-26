import pygame
import os
import sys

pygame.init()

screen_width = 1080
screen_height = 720
WHITE = (255, 255, 255)
IMAGENS_PARA_TRAS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_3.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_4.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_5.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_6.png'))),
]
IMAGENS_PARA_FRENTE = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_3.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_4.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_5.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/para_frente', 'imagem_6.png'))),
]
IMAGENS_SALTO = []

pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((screen_width, screen_height))


class Hadouken:
    def __init__(self, character):
        self.imagem = pygame.image.load(os.path.join('imgs', 'hadouken.png'))
        self.imagem = pygame.transform.scale_by(self.imagem, 0.15)
        self.rect = self.imagem.get_rect()
        self.rect.x = character.rect.x + character.rect.width // 2
        self.rect.y = character.rect.y + 75
        self.speed = 5
    
    def mover(self):
        self.rect.x += self.speed

class Bola:
    def __init__(self):
        self.imagem = pygame.image.load(os.path.join('imgs', 'bola.png'))
        self.imagem = pygame.transform.scale_by(self.imagem, 2.5)
        self.rect = self.imagem.get_rect()
        self.rect.x = 700
        self.rect.y = screen_height - 400

    def gravidade(self):
        if not self.on_ground:
            self.speed_y += 1
            
    def mover(self):
        self.rect.y += self.speed_y
        if self.rect.y >= screen_height - 50 - self.rect.height:
            self.rect.y = screen_height - 50 - self.rect.height
            self.speed_y = 0
            self.on_ground = True
    

    
    

class Character:
    def __init__(self, x, y): 
        self.imagem = IMAGENS_PARA_TRAS[0]
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 1
        self.on_ground = True
        self.hadouken = None
        
    def pular(self):
        if self.on_ground:
            self.speed_y -= 30
            self.on_ground = False
        
    def gravidade(self):
        if not self.on_ground:
            self.speed_y += 1
    
    def mover(self):
        self.rect.y += self.speed_y
        if self.rect.y >= screen_height - 50 - self.rect.height:
            self.rect.y = screen_height - 50 - self.rect.height
            self.speed_y = 0
            self.on_ground = True
    
    def lancar_hadouken(self):
        if self.hadouken is None or self.hadouken.rect.x > screen_width:
            self.hadouken = Hadouken(self)


class Ground:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (139, 69, 19)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


ground = Ground(0, screen_height - 50, screen_width, 50)
ryu = Character(100, 100)
bola = Bola()

# Define um retângulo de sprite para ele
ryu.rect.topleft = (100, screen_height - 150) 

# background
background = pygame.image.load(os.path.join('imgs', 'background.png'))
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()
background_rect.topleft = (0, 0)

clock = pygame.time.Clock()
delta_time = clock.tick(60) / 1000
speed = 12
tempo = 0
tempo_parado = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        if tempo == 0 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[0]
        if tempo == 1000 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[1]
        if tempo == 2000 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[2]
        if tempo == 3000 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[3]
        if tempo == 4000 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[4]
        if tempo == 5000 * delta_time:
            ryu.imagem = IMAGENS_PARA_TRAS[5]
            tempo = -1
        tempo += 1
        ryu.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        if tempo == 0 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[0]
        if tempo == 1000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[1]
        if tempo == 2000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[2]
        if tempo == 3000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[3]
        if tempo == 4000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[4]
        if tempo == 5000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[5]
            tempo = -1
        tempo += 1
        ryu.rect.x += speed
        
    if keys[pygame.K_UP]:
        ryu.pular()
    if keys[pygame.K_DOWN]:
        ryu.rect.y += ryu.speed_y

    if keys[pygame.K_x]:
        ryu.lancar_hadouken()
        
    if not any(keys):
        if tempo_parado == 0 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[0]
        elif tempo_parado == 3000 * delta_time:
            ryu.imagem = IMAGENS_PARA_FRENTE[5]
        elif tempo_parado == 6000 * delta_time:
            tempo_parado = -1
        tempo_parado += 1
    
    ryu.gravidade()
    ryu.mover()
    
    # limites da tela
    if ryu.rect.x < 0:
        ryu.rect.x = 0
    if ryu.rect.x > screen_width - ryu.rect.width:
        ryu.rect.x = screen_width - ryu.rect.width
    if ryu.rect.y < 0:
        ryu.rect.y = 0
    if ryu.rect.y > screen_height - ground.rect.height - ryu.rect.height:
        ryu.rect.y = screen_height - ground.rect.height - ryu.rect.height
        
    screen.fill(WHITE)
    ground.draw(screen)
    screen.blit(background, background_rect.topleft)
    
    if ryu.hadouken:
        ryu.hadouken.mover()
        if ryu.hadouken.rect.x < screen_width:
            screen.blit(ryu.hadouken.imagem, ryu.hadouken.rect.topleft)
        else:
            ryu.hadouken = None
    
    screen.blit(ryu.imagem, ryu.rect.topleft)
    screen.blit(bola.imagem, bola.rect.topleft)

    pygame.display.flip()
    clock.tick(60)

