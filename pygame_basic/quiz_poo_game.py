#충돌처리
import random
import pygame
############################
####기본 초기화 (필수)#######
pygame.init()

# window size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#window title
pygame.display.set_caption("poo game")

#FPS
clock = pygame.time.Clock()
################################

#1.사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)
#배경
background = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/background.png")

#캐릭터좌표
character = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = (screen_height) - (character_height)

#캐릭터 이동량
to_x,to_y = 0,0

#캐릭터 속도
character_speed = 0.6

#똥
poo = pygame.image.load("C:/Users/안정숙/Desktop/대학폴더/python work space/workplace/pygame_basic/enemy.png")
poo_size=poo.get_rect().size  #사각화해서 [가로길이, 세로길이] 저장
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos= random.randrange(0,screen_width-poo_width)
poo_y_pos= 0


#똥 속도
poo_speed = random.randrange(1,2)

running = True #active game
while running:
    dt = clock.tick(100) #게임 화면 초당 프레임수

    ###2. 이벤트 처리(키보드, 마우스 등)##################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #게임 더이상 실행 x

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
            elif event.key == pygame.K_UP and event.key == pygame.K_DOWN:
                to_y = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    
    #프레임 벗어나지 않게 하기
    if character_x_pos <0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

   
    #3. 게임 캐릭터 위치 처리####################
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    poo_y_pos += poo_speed *dt

    if poo_y_pos > screen_height-poo_height:
        poo_y_pos = 0
        poo_x_pos =random.randrange(0,screen_width-poo_width)
    #4. 충돌처리 ##################    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos #좌측 정보 업뎃
    poo_rect.top = poo_y_pos#위측 정보 업뎃

    if character_rect.colliderect(poo_rect):
        print("game over")
        running = False
    #5. 화면에 그리기 
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poo,(poo_x_pos,poo_y_pos))
    pygame.display.update() # redraw
    

#pygame종료
pygame.quit()