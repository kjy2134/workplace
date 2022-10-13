from turtle import _Screen
import pygame

pygame.init()

# window size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#window title
pygame.display.set_caption("nado game")

#background call
background=pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/background.png")

running = True #active game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #not active game

    screen.blit(background,(0,0)) # draw background
    pygame.display.update() # redraw
    
pygame.quit()