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
character_x_pos=(screen_width/2) - character_width/2

# 이동 좌표 값. 초기 좌표와 이동좌표값 따로 설정함
to_x, to_y = 0,0

# set character's width position half of window
character_y_pos=screen_height - character_height # set character's height position lowest 

#loof of event
running = True #active game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #게임 더이상 실행 x

        if event.type == pygame.KEYDOWN: #키가 눌렷는지 확인해서 눌리게 되면 좌표변경해주는거임
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP: # 키가 눌ㄹ지지 않았을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #최근 눌린 키값에 의해 더이상 움직이지 않게 하기 위해
            elif event.key ==  pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    character_x_pos += to_x
    character_y_pos += to_y

#가로 경계값 처리
    if character_x_pos <0:
        character_x_pos =0 
    elif character_x_pos > screen_width - character_width : #캐릭터 너비까지 뺴서 게임 경계에 못벗어나도록
        character_x_pos = screen_width - character_width
    
#세로 경계값 처리
    if character_y_pos <0: 
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height - character_height
    screen.blit(background,(0,0)) # draw background
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # redraw
    
pygame.quit()