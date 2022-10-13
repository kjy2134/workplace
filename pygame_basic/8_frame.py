#충돌처리
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



running = True #active game
while running:
    dt = clock.tick(30) #게임 화면 초당 프레임수

    ###2. 이벤트 처리(키보드, 마우스 등)##################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press QUIT button
            running = False #게임 더이상 실행 x

        
    #3. 게임 캐릭터 위치 처리####################
    
    #4. 충돌처리 ##################    

    #5. 화면에 그리기 
    pygame.display.update() # redraw
    

#pygame종료
pygame.quit()