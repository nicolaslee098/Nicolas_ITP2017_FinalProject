import random
import sys
import pygame.mixer
from pygame import *
from pygame.locals import *
from pygame.sprite import *
pygame.init()
pygame.mixer.music.load("Patakas World.wav")
pygame.mixer.music.play()
display.set_caption ('Ants')
screen = pygame.display.set_mode((800, 800))

class Ants(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('ant.png')
        self.rect = self.image.get_rect()
        randompos = random.randint(50,750)
        self.rect.center = (randompos,0)
    def Ants_appear (self):
        randompos = random.randint(50,750)
        self.rect.top = 0
        self.rect.left = randompos
    def ant_move_down(self):
        self.rect.top += 1

class Hammer(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('hammer-lv1.png')
        self.rect = self.image.get_rect()
        self.rect.center = mouse.get_pos()
    def hit (self, target):
        return self.rect.colliderect(target)
    def update(self):
        self.rect.center = mouse.get_pos()
    def upgrade1(self):
        self.image = image.load("hammer-lv2.png")
        self.rect = self.image.get_rect()
    def upgrade2(self):
        self.image = image.load("hammer-lv3.png")
        self.rect = self.image.get_rect()

class dead_ants(Sprite):
    def __init__(self,center):
        Sprite.__init__(self)
        self.image = image.load('dead ant.png')
        self.rect = self.image.get_rect()
        self.rect.center = center

class button_start(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,40)
        self.image = self.font.render ('Start',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,300)

class button_end(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Exit',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,600)

class button_easy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Easy',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,200)

class button_medium(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Medium',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,400)

class button_hard(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Hard',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,600)

class button_resume(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Resume',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,100)

class button_exit(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Exit',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,500)

class button_upgrade(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Upgrade',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,300)

class button_upgrade_lv2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Hammer lv.2 (3 Money)',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,300)

class button_upgrade_lv3(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Hammer lv.3 (6 Money)',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,600)

class button_main_menu(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Main Menu',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,700)

class button_back(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Back',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (375,700)

class button_try_again(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Try Again',1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (370,700)

def function():
    screen.fill((130, 82, 1))
    my_hammer.update()
    killedants.draw(screen)
    groupedants.draw(screen)
    all_sprites.draw(screen)
    scoreboard()
    missboard()
    timetext()
    bestscore()
    display.update()

def scoreboard ():
    font = pygame.font.Font(None,20)
    score_text = font.render ('Score: %d'%score,1,((0,0,0)))
    screen.blit(score_text,(375,750))

def missboard ():
    font = pygame.font.Font(None,20)
    miss_text = font.render ('Miss: %d'%miss,1,((0,0,0)))
    screen.blit(miss_text,(700,750))

def timetext():
    time_spent = (pygame.time.get_ticks() - initial_time) / 1000
    font = pygame.font.Font(None,20)
    time_text = font.render ('Time: %d' %time_spent, 1,(0,0,0))
    screen.blit(time_text,(70,750))

def moneyboard():
    font = pygame.font.Font(None,20)
    time_text = font.render ('Money: %d' %money, 1,(0,0,0))
    screen.blit(time_text,(70,750))

def bestscore():
    global best_score
    if score >= best_score:
        best_score = score
    font = pygame.font.Font(None,20)
    time_text = font.render ('Best Score: %d' %best_score, 1,(0,0,0))
    screen.blit(time_text,(375,30))

def gameovertext():
    gamebg = image.load ('gameo.jpg')
    screen.blit(gamebg,(0,0))

def not_enough_money():
    font = pygame.font.Font(None,40)
    time_text = font.render ('Not Enough Money!', 1,(0,0,0))
    screen.blit(time_text,(300,60))

def upgraded():
    font = pygame.font.Font(None,40)
    time_text = font.render ('Upgraded!', 1,(0,0,0))
    screen.blit(time_text,(300,100))

def pausegame():
    mouse.set_visible(True)
    gamepaused = True
    while gamepaused == True:
        upgradehammer = False
        showupgrade_initime = -pygame.time.get_ticks()
        shownomoney = -pygame.time.get_ticks()
        pausebg = image.load ('pause.jpg')
        screen.blit(pausebg,(0,0))
        moneyboard()
        esc_buttons.draw(screen)
        display.update()
        for i in event.get():
            if i.type == QUIT:
                pygame.quit()
                sys.exit()
            if i.type == MOUSEBUTTONDOWN:
                if Resume.rect.collidepoint(mouse.get_pos()):
                    gamepaused = False
                if Exit.rect.collidepoint(mouse.get_pos()):
                    pygame.quit()
                    exit()
                if Upgrade.rect.collidepoint(mouse.get_pos()):
                    upgradehammer = True
                if Main_menu.rect.collidepoint(mouse.get_pos()):
                    global second
                    global third
                    second = False
                    third = False
                    gamepaused = False

                while upgradehammer == True:
                    global money
                    global my_hammer
                    gamepaused = True

                    for i in event.get():
                        if i.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if i.type == MOUSEBUTTONDOWN:
                            if Upgrade_lv2.rect.collidepoint(mouse.get_pos()):
                                if money >= 3:
                                    money -= 3
                                    my_hammer.upgrade1()
                                    showupgrade_initime = pygame.time.get_ticks()
                                    display.update()
                                elif money <=3:
                                    shownomoney = pygame.time.get_ticks()
                                    display.update()
                            elif Upgrade_lv3.rect.collidepoint(mouse.get_pos()):
                                if money >= 6:
                                    money -=6
                                    showupgrade_initime = pygame.time.get_ticks()
                                    my_hammer.upgrade2()
                                    display.update()
                                elif money <=6:
                                    shownomoney = pygame.time.get_ticks()
                                    display.update()
                            elif Back.rect.collidepoint(mouse.get_pos()):
                                upgradehammer = False
                        if i.type == KEYDOWN:
                            if i.key == K_ESCAPE:
                                gamepaused = False

                    upgradebg = image.load ('up.jpg')
                    screen.blit(upgradebg,(0,0))
                    if pygame.time.get_ticks() - showupgrade_initime <= 2000:
                        upgraded()
                    if pygame.time.get_ticks() - shownomoney <=2000:
                        not_enough_money()
                    moneyboard()
                    upgrade_buttons.draw(screen)
                    display.update()

            if i.type == KEYDOWN:
                if i.key == K_ESCAPE:
                    gamepaused = False

global best_score
best_score = 0
maingame = True
while maingame:
    global my_hammer
    global money
    score = 0
    miss = 0
    money = 0
    score_for_money = 0
    initial_time = pygame.time.get_ticks()
    my_hammer = Hammer()
    killedants = Group()
    Start = button_start()
    End = button_end()
    Easy = button_easy()
    Medium = button_medium()
    Hard = button_hard()
    Resume = button_resume()
    Exit = button_exit()
    Upgrade = button_upgrade()
    Upgrade_lv2 = button_upgrade_lv2()
    Upgrade_lv3 = button_upgrade_lv3()
    Main_menu = button_main_menu()
    Back = button_back()
    Try_again = button_try_again()
    all_sprites = Group(my_hammer)
    main_buttons = Group(Start, End)
    buttons = Group(Easy, Medium, Hard)
    esc_buttons = Group (Resume, Exit, Upgrade, Main_menu)
    upgrade_buttons = Group (Upgrade_lv2,Upgrade_lv3, Back)
    last_button = Group (Try_again)

    first = True
    while first:
        startbg = image.load ('start bg.png')
        screen.blit(startbg,(0,0))
        main_buttons.draw(screen)
        display.update()
        for ev in event.get():
            if ev.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if Start.rect.collidepoint(mouse.get_pos()):
                    first = False
                elif End.rect.collidepoint(mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

    mainbg = image.load ('as.jpg')
    screen.blit(mainbg,(0,0))
    display.update()
    buttons.draw(screen)
    display.update()
    global second
    global third
    second = True
    third = True
    game_running = False
    antimer = pygame.time.get_ticks()
    gamemode = None
    gamepaused = False
    groupedants = Group()

    while second:
        for i in event.get():
            if i.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if i.type == MOUSEBUTTONDOWN:
                if Easy.rect.collidepoint(mouse.get_pos()):
                    game_running = True
                    gamemode = 1
                elif Medium.rect.collidepoint(mouse.get_pos()):
                    game_running=True
                    gamemode = 2
                elif Hard.rect.collidepoint(mouse.get_pos()):
                    game_running=True
                    gamemode = 3

        if game_running == True:
            function()
            if gamemode == 1:
                for ev in event.get():
                    timetext()
                    if ev.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if ev.type == MOUSEBUTTONDOWN:
                        for ant in groupedants:
                            if ant.rect.colliderect(my_hammer):
                                pygame.mixer.music.load("Slap-SoundMaster13-49669815.wav")
                                mixer.music.play()
                                killedants.add(dead_ants(ant.rect.center))
                                groupedants.remove(ant)
                                score += 1
                                score_for_money += 1
                                if score_for_money >= 10:
                                    money += 1
                                    score_for_money -= 10
                    if ev.type == KEYDOWN:
                        if ev.key == K_ESCAPE:
                            pausegame()
                if pygame.time.get_ticks() - antimer >= 1000:
                    tempant = Ants() #temp=temporary
                    groupedants.add(tempant)
                    antimer = pygame.time.get_ticks()

                for ant in groupedants:
                    ant.ant_move_down()
                    if ant.rect.top == 800:
                        miss += 1

            if gamemode == 2:
                for ev in event.get():
                    if ev.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if ev.type == MOUSEBUTTONDOWN:
                        for ant in groupedants:
                            if ant.rect.colliderect(my_hammer):
                                pygame.mixer.music.load("Slap-SoundMaster13-49669815.wav")
                                mixer.music.play()
                                killedants.add(dead_ants(ant.rect.center))
                                groupedants.remove(ant)
                                score += 1
                                score_for_money += 1
                                if score_for_money >= 10:
                                    money += 1
                                    score_for_money -= 10
                    if ev.type == KEYDOWN:
                        if ev.key == K_ESCAPE:
                            pausegame()
                if pygame.time.get_ticks() - antimer >= 500:
                    tempant = Ants()
                    groupedants.add(tempant)
                    antimer = pygame.time.get_ticks()

                for ant in groupedants:
                    ant.ant_move_down()
                    if ant.rect.top == 800:
                        miss += 1

            if gamemode == 3:
                for ev in event.get():
                    if ev.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if ev.type == MOUSEBUTTONDOWN:
                        for ant in groupedants:
                            if ant.rect.colliderect(my_hammer):
                                pygame.mixer.music.load("Slap-SoundMaster13-49669815.wav")
                                mixer.music.play()
                                killedants.add(dead_ants(ant.rect.center))
                                groupedants.remove(ant)
                                score += 1
                                score_for_money += 1
                                if score_for_money >= 10:
                                    money += 1
                                    score_for_money -= 10
                    if ev.type == KEYDOWN:
                        if ev.key == K_ESCAPE:
                            pausegame()

                if pygame.time.get_ticks() - antimer >= 100:
                    tempant = Ants()
                    groupedants.add(tempant)
                    antimer = pygame.time.get_ticks()

                for ant in groupedants:
                    ant.ant_move_down()
                    if ant.rect.top == 800:
                        miss += 1
            if miss >= 10:
                second = False
            mouse.set_visible(False)
    while third:
        mouse.set_visible(True)
        gameovertext()
        last_button.draw(screen)
        display.update()
        for ev in event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if Try_again.rect.collidepoint(mouse.get_pos()):
                    third = False
    mouse.set_visible(True)
