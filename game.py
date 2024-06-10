import pygame
import sys

pygame.init()

screen_width = 600
screen_height = 800

WHITE = (255,255,255)

pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((screen_width, screen_height))
ryu = pygame.image.load('imgs\minha_imagem.jpeg')

#define um retangulo de sprite pra ele

ryu_rect = ryu.get_rect()
ryu_rect.topleft = (100,100)

speed = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed() #retorna uma lista de booleanos relacionados a cada uma das teclas do teclado

    if keys[pygame.K_LEFT]:
            ryu_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        ryu_rect.x += speed
    if keys[pygame.K_UP]:
        ryu_rect.y -= speed
    if keys[pygame.K_DOWN]:
        ryu_rect.y += speed

    screen.fill(WHITE)
    screen.blit(ryu, ryu_rect.topleft)
    pygame.display.flip()