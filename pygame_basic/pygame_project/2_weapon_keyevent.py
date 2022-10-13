#충돌처리
import os
import pygame
############################
####기본 초기화 (필수)#######
pygame.init()

# window size
screen_width = 640  
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#window title
pygame.display.set_caption("pang game")

#FPS
clock = pygame.time.Clock()
################################

#1.사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일 위치 반환
image_path = os.path.join(current_path,"pygame_images") #images 폴더 위치 반환

#배경
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height-character_height-stage_height

#캐릭터 이동속도
character_speed = 5

#캐릭터 이동 좌표값
to_x, to_y = 0,0

#무기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기 여러발 발사
weapons = []

#무기 이동속도
weapon_speed=10

running = True #active game
while running:
    dt = clock.tick(30) #게임 화면 초당 프레임수

    ###2. 이벤트 처리(키보드, 마우스 등)##################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #게임 더이상 실행 x

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    #3. 게임 캐릭터 위치 처리####################
    character_x_pos += to_x

    #경계값 설정
    if character_x_pos <0 :
        character_x_pos =0
    elif character_x_pos > screen_width-character_width :
        character_x_pos = screen_width-character_width

    #무기 위치 조정
    weapons = [ [ w[0],w[1]-weapon_speed] for w in weapons if w[1]>0] #y좌표가 0이상인것만 리스트로 저장

    #4. 충돌처리 ##################    

    #5. 화면에 그리기 
    screen.blit(background,(0,0))
    for weapon_x_pos,weapon_y_pos in weapons: #리스트 내 원소를 각각 무기 X,Y좌표로 받기
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    

    pygame.display.update() # redraw
    

#pygame종료
pygame.quit()

