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

#call character 
character = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/character.png")
character_size = character.get_rect().size # size of image
character_width = character_size[0] # size of width
character_height = character_size[1] # size of height
character_x_pos=(screen_width/2) - character_width/2 # set character's width position half of window
character_y_pos=screen_height - character_height # set character's height position lowest 

#loof of event
running = True #active game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #not active game

    screen.blit(background,(0,0)) # draw background
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # redraw
    
pygame.quit()