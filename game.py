import pygame
import os
import sys

pygame.init()

screen_width = 1080
screen_height = 720
WHITE = (255, 255, 255)
IMAGENS_PARADO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_3.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_4.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_5.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs/parado', 'imagem_6.png'))),
]

pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((screen_width, screen_height))


class Hadouken:
    def __init__(self, Character):
        self.imagem = pygame.image.load(os.path.join('imgs','hadouken.jpg'))
        self.x = Character.x
        self.y = Character.y
        self.speed = 0.7
    def mover(self):
        self.x += self.speed
    

class Character:
    def __init__(self, x, y): 
        self.imagem = IMAGENS_PARADO[0]
        self.rect = self.imagem.get_rect()
        self.x = x
        self.y = y
        self.speed_y = 0
        self.on_ground = True
        
    def pular(self):
        # tenho que adicionar gravidade e fazer a animação de mortal do pulo
        if(self.on_ground):
            self.speed_y -= 4.5
            self.on_ground = False
        
    def gravidade(self):
        if not self.on_ground:
            self.speed_y += 0.03
    
    def mover(self):
        self.rect.y += self.speed_y
        if self.rect.y >= screen_height - 50 - self.rect.height:
            self.rect.y = screen_height - 50 - self.rect.height
            self.speed_y = 0
            self.on_ground = True
    
    def hadouken(self):
        hadouken_gerado = Hadouken(0,self)
        hadouken_gerado.x += speed
        
class Ground:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (139, 69, 19)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


ground = Ground(0, screen_height - 50, screen_width, 50)

ryu = Character(100, 100)

# Define um retângulo de sprite para ele
ryu.rect.topleft = (100, screen_height - 150) 

#background
background = pygame.image.load(os.path.join('imgs','background.png'))
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()
background_rect.topleft = (0,0)

speed = 1
tempo = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        ryu.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        ryu.rect.x += speed
    if keys[pygame.K_UP]:
        ryu.pular()
    if keys[pygame.K_DOWN]:
        ryu.rect.y += speed
    
    ryu.gravidade()    
    ryu.mover()
    
    #limites da tela

    if ryu.rect.x < 0:
        ryu.rect.x = 0
    if ryu.rect.x > screen_width - ryu.rect.width:
        ryu.rect.x = screen_width - ryu.rect.width
    if ryu.rect.y < 0:
        ryu.rect.y = 0
    if ryu.rect.y > screen_height - ground.rect.height - ryu.rect.height:
        ryu.rect.y = screen_height - ground.rect.height - ryu.rect.height
        
    #animação dele parado
    
    delta = 150
    
    if tempo == 0*delta:
        ryu.imagem = IMAGENS_PARADO[0]
    if tempo == 1*delta:
        ryu.imagem = IMAGENS_PARADO[1]
    if tempo == 2*delta:
        ryu.imagem = IMAGENS_PARADO[2]
    if tempo == 3*delta:
        ryu.imagem = IMAGENS_PARADO[3]
    if tempo == 4*delta:
        ryu.imagem = IMAGENS_PARADO[4]
    if tempo == 5*delta:
        ryu.imagem = IMAGENS_PARADO[5]
        tempo = -1
    
    tempo += 1

    screen.fill(WHITE)
    ground.draw(screen)  # Desenha o chão
    screen.blit(background, background_rect.topleft)
    screen.blit(ryu.imagem, ryu.rect.topleft)  # Desenha a imagem na nova posição
    pygame.display.flip()

