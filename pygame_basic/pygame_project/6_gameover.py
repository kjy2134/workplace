# 1. 모든 공 없애면
# 2. 캐릭터가 공에 닿으면
# 3. 시간 제한 99초 초과시

from email.iterators import body_line_iterator
import os
from sys import displayhook
from tkinter import N
from tkinter.messagebox import NO
from turtle import delay
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

#공 만들기( 4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path,("balloon1.png"))),
    pygame.image.load(os.path.join(image_path,("balloon2.png"))),
    pygame.image.load(os.path.join(image_path,("balloon3.png"))),
    pygame.image.load(os.path.join(image_path,("balloon4.png")))
]

#공 크기에 따른 최초 스피드(공이 클수록 스피드가 큼)
ball_speed_y= [-18,-15,-12,-9] #index 0,1,2,3에 해당하는 값 : 각 공의 초기 속도

#공들
balls = []

#최초 발생 큰공 추가
balls.append({
    "pos_x":50, #공의 x좌표
    "pos_y":50, #공의 y좌표
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x": 3, #x축 이동방향, -면 왼쪽 +면 오른쪽으로 이동
    "to_y":-6, #y축 이동방향
    "init_spd_y" : ball_speed_y[0] #y 최초속도
})

#사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

#폰트 정의
game_font = pygame.font.Font(None,40)
total_time = 100
start_ticks = pygame.time.get_ticks() #시작 시간 정의

#게임 종료 메세지
#Time out(시간 초과 실패)
#Mission complete(성공)
#game over(캐릭 공에 맞음, 실패)
game_result= "Game Over"

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

    #공 위치 정의
    for ball_idx,ball_val in enumerate(balls): #enumerate(list) =>(list의 index값, 해당 index에 저장된 값) 형태로 정리해주는 함수 
        # ball_idx -> index //ball_val -> 원소값 저장
        ball_pos_x = ball_val["pos_x"]
        ball__pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

    #가로 벽 닿았을 때 공 위치 변경 ( 튕겨 나오는 효과 위해 방향 바꿔줌)
        if ball_pos_x <0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"]*-1 
    
    #위아래로 튕김
        if ball__pos_y >= screen_height-stage_height-ball_height :
            ball_val["to_y"] = ball_val["init_spd_y"] #스테이지에 튕겨 올라가는 처리 (stage에 닿았을 때 to_y가 초기속도 -18로 바뀌어서 다시 올라감)
        else: # 그 외의 경우 공의 속도 증가
            ball_val["to_y"] += 0.5 # to_y가 -18 .. -17 ..-1 .. 0 .. 1 .. 2 로 바뀌면서 포물선 처럼 그리게 됨 올라갔다 내려가는 효과

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    #4. 충돌처리 ##################    

    #캐릭터 rect 정보 업뎃
    chracter_rect = character.get_rect()
    chracter_rect.left = character_x_pos
    chracter_rect.top=character_y_pos

    for ball_idx,ball_val in enumerate(balls): #enumerate(list) =>(list의 index값, 해당 index에 저장된 값) 형태로 정리해주는 함수 
        # ball_idx -> index //ball_val -> 원소값 저장
        ball_pos_x = ball_val["pos_x"]
        ball__pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect정보 업뎃
        ball_rect = ball_images[ball_img_idx].get_rect() 
        ball_rect.left = ball_pos_x
        ball_rect.top = ball__pos_y

        #공과 캐릭터 충돌 체크
        if chracter_rect.colliderect(ball_rect):
            running = False
            break

        #공과 무기의 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            #무기 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left=weapon_x_pos
            weapon_rect.top = weapon_y_pos

            #충돌 체크 
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx#해당 공 없개익 위한 값 설정

                #가장 작은 공이 아니라면 다음 단계 공으로 나누기
                if ball_img_idx < 3:
                    #현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect() #리스ㅋ트로 저장한 공들 정보 중 다음 공 불러오기
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({ #왼쪽으로 튕겨나가는 공
                        "pos_x":ball_pos_x + (ball_width/2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y":ball__pos_y + (ball_height/2) - (small_ball_height / 2), #공의 y좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x": -3, #x축 이동방향, -면 왼쪽 +면 오른쪽으로 이동
                        "to_y":-6, #y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx+1] #y 최초속도
                        })
                    balls.append({ #오른쪽으로 튕기는 공
                        "pos_x":ball_pos_x + (ball_width/2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y":ball__pos_y + (ball_height/2) - (small_ball_height / 2) , #공의 y좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x": 3, #x축 이동방향, -면 왼쪽 +면 오른쪽으로 이동
                        "to_y":-6, #y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx+1] #y 최초속도
                        })
                break
        else: 
            continue
        break
    #충돌한 공과 무기 없애기
    if ball_to_remove >-1 :
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1: 
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    #모든 공 없앤 경우 종료
    if len(balls) == 0:
        game_result = "Mission complete"
        running = False

    #5. 화면에 그리기 
    screen.blit(background,(0,0))
    for weapon_x_pos,weapon_y_pos in weapons: #리스트 내 원소를 각각 무기 X,Y좌표로 받기
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx,val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball__pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball__pos_y))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("TIME :  {} ".format(int(total_time-elapsed_time)),True, (255,255,0))
    screen.blit(timer,(10,10))

    #시간 초과 시
    if total_time - elapsed_time <0 :
        game_result = "Time over"
        running = False

    pygame.display.update() # redraw

#게임 오버 메세지
msg = game_font.render(game_result,True,(0,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2))) #center변수로 화면 가운데 좌표값 얻어오기
screen.blit(msg, msg_rect)
pygame.display.update() #업데이트를 해야 화면에 반영 됨
# 화면 대기
pygame.time.delay(2000)

#pygame종료
pygame.quit()

