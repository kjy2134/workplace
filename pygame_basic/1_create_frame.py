import pygame

pygame.init()

# window size
screen_width = 480
screen_height = 640
screen=pygame.display.set_mode((screen_width,screen_height))

#window title
pygame.display.set_caption("nado game")

running = True #active game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #not active game


pygame.quit()