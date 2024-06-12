import pygame
import os
import sys

pygame.init()

screen_width = 600
screen_height = 800
WHITE = (255, 255, 255)

pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((screen_width, screen_height))

ryu = pygame.image.load(os.path.join('imgs', 'minha_imagem.jpeg'))

# Define um retângulo de sprite para ele
ryu_rect = ryu.get_rect()
ryu_rect.topleft = (100, screen_height - 150) 

speed = 1 

class Ground:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (139, 69, 19)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


ground = Ground(0, screen_height - 50, screen_width, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ryu_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        ryu_rect.x += speed
    if keys[pygame.K_UP]:
        ryu_rect.y -= speed
    if keys[pygame.K_DOWN]:
        ryu_rect.y += speed

    if ryu_rect.x < 0:
        ryu_rect.x = 0
    if ryu_rect.x > screen_width - ryu_rect.width:
        ryu_rect.x = screen_width - ryu_rect.width
    if ryu_rect.y < 0:
        ryu_rect.y = 0
    if ryu_rect.y > screen_height - ground.rect.height - ryu_rect.height:
        ryu_rect.y = screen_height - ground.rect.height - ryu_rect.height

    screen.fill(WHITE)
    ground.draw(screen)  # Desenha o chão
    screen.blit(ryu, ryu_rect.topleft)  # Desenha a imagem na nova posição
    pygame.display.flip()

