#하늘에서 떨어지는 똥 피하기 게임

#[조건]
#1) 캐릭터는 화면 가장 아래에 위치, 좌우로 이동가능
#2) 똥은 화면 가장 위에서 떨어짐, X좌표는 매번 랜덤으로 설정
#3) 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
#4) 캐릭터와 똥이 충돌하면 게임이 종료
#5) FPS는 30으로 고정

#[게임이미지]
#배경 : 480* 640(가로세로)
#캐릭터 : 70*70
#똥 : 70* 70

import pygame #pip install pygame으로 설치
import random
pygame.init()#초기화

#화면크기설정 및 기초설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("DDong Pihagi~")
clock = pygame.time.Clock()

#캐릭터불러오기
background = pygame.image.load("D:/#Folder#/유익/Programming/Python공부/Game/Quiz01/background.png")

character = pygame.image.load("D:/#Folder#/유익/Programming/Python공부/Game/Quiz01/character.png")
character_size = character.get_rect().size
character_width = character_size[0]#가로크기
character_height = character_size[1]#세로크기
character_x_pos = (screen_width/2)-character_width/2 #화면가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면세로크기가장아래

#적불러오기
enemy = pygame.image.load("D:/#Folder#/유익/Programming/Python공부/Game/Quiz01/enemy.png")
enemy_size = enemy.get_rect().size #이미지크기구하기
enemy_width = enemy_size[0]#가로크기
enemy_height = enemy_size[1]#세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) #화면가로의 절반크기에 해당하는 곳에 위치
enemy_y_pos = 0 #화면세로크기가장아래


#이동할 좌표
to_x =0
to_y = 0

#케릭터속도
character_speed = 1

#폰트정의
game_font = pygame.font.Font(None, 40) #폰트객체생성 (폰트(디폴트값), 크기)

#게임 제한시간
total_time = 30 
#시간계산
start_ticks = pygame.time.get_ticks() #시작tick 받기


#이벤트루프
running = True #게임실행중인가

while running:
    dt = clock.tick(30)  #30프레임
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0


    character_x_pos += to_x* dt
    enemy_y_pos += 10



    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    if  enemy_y_pos > screen_height :
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    #rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect): #만나면 게임종료
        print("SSHHHHHIT!!")
        running =False
       
    #게임시간 및 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))


    #만약 시간이 0이하면 게임종료
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False


    #스크린에 객체 불러오기
    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))#캐릭터그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))#적군그리기
    screen.blit(timer,(10,10))
    pygame.display.update()#게임화면다시그리기


pygame.quit()