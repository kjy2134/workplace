#충돌처리

from ast import If
import pygame

pygame.init()

# window size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#window title
pygame.display.set_caption("nado game")

#FPS
clock = pygame.time.Clock()
#background call
background=pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/background.png")

#call character 
character = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/character.png")
character_size = character.get_rect().size # size of image
character_width = character_size[0] # size of width
character_height = character_size[1] # size of height
character_x_pos=(screen_width/2) - character_width/2# set character's width position half of window
character_y_pos=screen_height - character_height # set character's height position lowest 
# 이동 좌표 값. 초기 좌표와 이동좌표값 따로 설정함
to_x, to_y = 0,0

#이동속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # size of image
enemy_width =enemy_size[0] # size of width
enemy_height = enemy_size[1] # size of height
enemy_x_pos=(screen_width/2) - enemy_width/2
enemy_y_pos=(screen_height/2) - (enemy_height/2) # set character's height position lowest 
#화면 가운데 적을 세팅


#loof of event
running = True #active game
while running:
    dt = clock.tick(30) #게임 화면 초당 프레임수

#캐릭터가 1초동안 100만큼 이동해야 한다면
#10fps: 1초동안 10번 동작 -> 1번에 10만큼 이동 10*10 =100
#20fps : 1초동안 20번 동작해야 -> 1번에 5만큼 20*5 =100

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #게임 더이상 실행 x

        if event.type == pygame.KEYDOWN: #키가 눌렷는지 확인해서 눌리게 되면 좌표변경해주는거임
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 키가 눌ㄹ지지 않았을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #최근 눌린 키값에 의해 더이상 움직이지 않게 하기 위해
            elif event.key ==  pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    character_x_pos += to_x *dt #속도 보정을 위함 프레임 증가 감소 여부 상관 없이 이동 속도 유지 하기 위함.
    character_y_pos += to_y *dt

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
    
#충돌처리 위한 rect정보 업뎃
    character_rect = character.get_rect()#x,y좌표값 가지고 있음 네모화
    character_rect.x = character_x_pos #화면상 왼쪽
    character_rect.y = character_y_pos # 화면상 맨 위

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
# enemy가 실제로 움직이지 않지만 enemy_Rect에 값을 반영하기위해 변수선언

 
#충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
    
    screen.blit(background,(0,0)) # draw background
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    pygame.display.update() # redraw
    
pygame.quit()