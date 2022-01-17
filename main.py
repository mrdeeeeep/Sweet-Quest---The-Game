import pygame
import time
from pygame import mixer
import pynput



screen_x = 1239
screen_y = 717


pygame.mixer.init(44100, -16, 1, 1024)
pygame.init()

pygame.display.set_caption("Sweet Quest")


screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()





bg = (235, 235, 235)
player_posx = 0
player_posy = 280
frame_count = 0
sleep = 0.04
movement_speed = 8
cluescreen = None
volume = 0.5
keep_playing = True

runRight = [pygame.image.load('Assets/Characters/Run_01.png'),
            pygame.image.load('Assets/Characters/Run_02.png'),
            pygame.image.load('Assets/Characters/Run_03.png'),
            pygame.image.load('Assets/Characters/Run_04.png'),
            pygame.image.load('Assets/Characters/Run_05.png'),
            pygame.image.load('Assets/Characters/Run_06.png'),
            pygame.image.load('Assets/Characters/Run_07.png'),
            pygame.image.load('Assets/Characters/Run_08.png')]

runLeft = [pygame.transform.flip(runRight[0], True, False),
           pygame.transform.flip(runRight[1], True, False),
           pygame.transform.flip(runRight[2], True, False),
           pygame.transform.flip(runRight[3], True, False),
           pygame.transform.flip(runRight[4], True, False),
           pygame.transform.flip(runRight[5], True, False),
           pygame.transform.flip(runRight[6], True, False),
           pygame.transform.flip(runRight[7], True, False)]

runIdle = pygame.image.load("Assets/Characters/Idle.png")

img_scene_hallway = pygame.image.load('Assets/Scenes/hallway.png')
img_scene_clueroom = pygame.image.load('Assets/Scenes/clue room.png')
img_scene_questroom = pygame.image.load('Assets/Scenes/quest room.png')
img_scene_quest_cat = pygame.image.load('Assets/Scenes/quest cat.png')
img_scene_questlion = pygame.image.load('Assets/Scenes/quest lion.png')
img_scene_questpanda = pygame.image.load('Assets/Scenes/quest panda.png')
img_scene_questmonkey = pygame.image.load('Assets/Scenes/quest monkey.png')
img_scene_cluescreen = pygame.image.load('Assets/Scenes/clue screen.png')

img_victory = pygame.image.load('Assets/Scenes/victory.png')

door_sound = mixer.Sound('Assets/Audio/opendoor.wav')
door_sound.set_volume(volume)


"""SCREENS"""
mainmenu = True
mainGameLoop = True
scene_hallway = True
scene_clueroom = False
scene_questroom = False





def pygameQUIT():
    global mainmenu, mainGameLoop, scene_hallway, scene_questroom, scene_clueroom
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainmenu = False
            mainGameLoop = False
            scene_hallway = False
            scene_clueroom = False
            scene_questroom = False


def characterMOVEMENT():
    global frame_count, player_posx, player_posy, active_scene
    screen.blit(runIdle, (player_posx, player_posy))
    keys = pygame.key.get_pressed()


    if keys[pygame.K_d]:
        screen.blit(active_scene, (0, 0))
        player_posx += movement_speed
        time.sleep(sleep)
        if frame_count == 7:
            frame_count = 0
        frame_count += 1
        screen.blit(runRight[frame_count], (player_posx, player_posy))

    if keys[pygame.K_a]:
        screen.blit(active_scene, (0, 0))
        player_posx -= movement_speed
        time.sleep(sleep)
        if frame_count == 7:
            frame_count = 0
        frame_count += 1
        screen.blit(runLeft[frame_count], (player_posx, player_posy))

    if player_posx > 1120:
        player_posx = 1120
    if player_posx < -30:
        player_posx = -30




'''main menu'''
def startMenu():
    bit_font_big = pygame.font.Font('Assets/Font/bitfont.ttf', 24)
    start_text = bit_font_big.render('START', True, (0, 0, 0,))
    screen.blit(start_text, (550, 300))

    bit_font_small = pygame.font.Font('Assets/Font/bitfont.ttf', 14)
    tutorial_text = bit_font_small.render('PRESS "A" AND "D" TO MOVE and PRESS "ENTER" TO INTERACT', True, (0, 0, 0))
    screen.blit(tutorial_text, (170, 150))

def playmusic():
    global bg_song
    bg_song = mixer.Sound('Assets/Audio/bg.mp3')
    bg_song.set_volume(volume)
    bg_song.play()


playmusic()
while mainmenu:
    pygameQUIT()
    screen.fill(bg)
    startMenu()
    screen.blit(runIdle, (player_posx, player_posy))

    keys = pygame.key.get_pressed()
    movement_speed = 8

    if keys[pygame.K_d]:
        screen.fill(bg)
        startMenu()
        player_posx += movement_speed
        time.sleep(sleep)
        if frame_count == 7:
            frame_count = 0
        frame_count += 1
        screen.blit(runRight[frame_count], (player_posx, player_posy))

    if keys[pygame.K_a]:
        screen.fill(bg)
        startMenu()
        player_posx -= movement_speed
        time.sleep(sleep)
        if frame_count == 7:
            frame_count = 0
        frame_count += 1
        screen.blit(runLeft[frame_count], (player_posx, player_posy))

    if player_posx >1120:
        player_posx = 1120
    if player_posx < -30:
        player_posx = -30

    if keys[pygame.K_RETURN]:
        if player_posx > 480 and player_posx < 640:
            door_sound.play()
            mainmenu = False
            mainGameLoop = True
            scene_hallway = True




    pygame.display.update()
    clock.tick(30)




'''main game loop'''

while mainGameLoop:
    global bg_song

    bg_song.stop()
    '''HALLWAY'''
    def hallwayDoorInteraction():
        global scene_hallway, scene_clueroom, scene_questroom, player_posx
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if player_posx > 260 and player_posx < 430:
                door_sound.play()
                scene_hallway = False
                scene_clueroom = True
                time.sleep(0.1)
                player_posx = 80
            if player_posx > 820 and player_posx < 960:
                door_sound.play()
                scene_hallway = False
                scene_questroom = True
                time.sleep(0.1)
                player_posx = 80

    while scene_hallway:
        movement_speed = 8
        screen.blit(img_scene_hallway, (0,0))
        pygameQUIT()
        active_scene = img_scene_hallway
        characterMOVEMENT()
        hallwayDoorInteraction()
        pygame.display.update()


    '''CLUEROOM'''
    time1, time2, dtime = 0 ,0 , 0

    while scene_clueroom:
        movement_speed = 13
        pygameQUIT()
        sleep = 0.03
        active_scene = img_scene_clueroom
        screen.blit(img_scene_clueroom, (0,0))
        characterMOVEMENT()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_posx > -30 and player_posx < 110:
                        door_sound.play()
                        scene_clueroom = False
                        scene_hallway = True
                        time.sleep(0.1)
                        player_posx = 400


                    if player_posx > 175 and player_posx < 330:
                        cluescreen = "active"
                        clue1 = mixer.Sound('Assets/Audio/clue1.mp3')
                        clue1.set_volume(volume)
                        clue1.play()
                    if player_posx > 470 and player_posx < 630:
                        cluescreen = 'active'
                        clue2 = mixer.Sound('Assets/Audio/clue2.mp3')
                        clue2.set_volume(volume)
                        clue2.play()
                    if player_posx > 755 and player_posx < 985:
                        cluescreen = 'active'
                        clue3 = mixer.Sound('Assets/Audio/clue3.mp3')
                        clue3.set_volume(volume)
                        clue3.play()
                    if player_posx == 1120:
                        cluescreen = 'active'
                        clue4 = mixer.Sound('Assets/Audio/clue4.mp3')
                        clue4.set_volume(volume)
                        clue4.play()

                    time1 = time.time()

        while cluescreen == 'active':
            pygameQUIT()
            screen.blit(img_scene_cluescreen, (0,0))
            time2 = time.time()
            dtime = time2 - time1
            dtime = round(dtime)
            if dtime == 3:
                cluescreen = None

            pygame.display.update()



        pygame.display.update()




    '''QUESTROOM'''
    quest_completed = 0
    lion_completed = False
    cat_completed = False
    monkey_completed = False
    panda_completed = False
    questscreen_lion , questscreen_cat, questscreen_monkey, questscreen_panda = False, False, False, False

    def victory():
        global quest_completed

        if quest_completed == 4:
            victory_sound = mixer.Sound('Assets/Audio/victory_sound.mp3')
            victory_sound.play()
            while True:
                screen.blit(img_victory, (0,0))
                pygameQUIT()



                pygame.display.update()

    def mainQuest():
        global quest_completed, lion_completed, panda_completed, cat_completed, monkey_completed
        global questscreen_monkey, questscreen_panda, questscreen_cat, questscreen_lion

        level_error = mixer.Sound('Assets/Audio/level failed.wav')
        level_error.set_volume(volume)
        level_passed = mixer.Sound('Assets/Audio/level passed.wav')
        level_passed.set_volume(volume)

        '''lion quest'''
        while questscreen_lion:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    if mouse_posx > 650 and mouse_posx < 930 and lion_completed == False:
                        if mouse_posy > 223 and mouse_posy < 520:
                            if mouse_posy > 453 and mouse_posy < 470:
                                level_passed.play()
                                lion_completed = True
                                quest_completed += 1
                                questscreen_lion = False
                            else:
                                level_error.play()
                                questscreen_lion = False
                                wrongAlert()
            pygameQUIT()
            screen.blit(img_scene_questlion, (0, 0))
            pygame.display.update()

        '''panda quest'''
        while questscreen_panda:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    if mouse_posx > 650 and mouse_posx < 930 and panda_completed == False:
                        if mouse_posy > 223 and mouse_posy < 520:
                            if mouse_posy > 320 and mouse_posy < 340:
                                level_passed.play()
                                panda_completed = True
                                quest_completed += 1
                                questscreen_panda = False
                            else:
                                level_error.play()
                                questscreen_panda = False
                                wrongAlert()
            pygameQUIT()
            screen.blit(img_scene_questpanda, (0, 0))
            pygame.display.update()


        '''monkey quest'''
        while questscreen_monkey == True and scene_questroom == True :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    if mouse_posx > 650 and mouse_posx < 930 and monkey_completed == False:
                        if mouse_posy > 223 and mouse_posy < 520:
                            if mouse_posy > 410 and mouse_posy < 430:
                                level_passed.play()
                                monkey_completed = True
                                quest_completed += 1
                                questscreen_monkey = False
                            else:
                                level_error.play()
                                questscreen_monkey = False
                                wrongAlert()
            pygameQUIT()
            screen.blit(img_scene_questmonkey, (0, 0))
            pygame.display.update()

        '''cat quest'''
        while questscreen_cat:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    if mouse_posx > 650 and mouse_posx < 930 and cat_completed == False:
                        if mouse_posy > 223 and mouse_posy < 520:
                            if mouse_posy > 223 and mouse_posy < 250:
                                level_passed.play()
                                cat_completed = True
                                quest_completed += 1
                                questscreen_cat = False
                            else:
                                level_error.play()
                                questscreen_cat = False
                                wrongAlert()
            pygameQUIT()
            screen.blit(img_scene_quest_cat, (0, 0))
            pygame.display.update()



    def wrongAlert():
        wrongAlertScreen = True
        bit_font_small = pygame.font.Font('Assets/Font/bitfont.ttf', 22)
        tutorial_text = bit_font_small.render('WRONG! Look for clues in the other room!', True, (255, 255, 255))
        time1 = time.time()
        while wrongAlertScreen:
            pygameQUIT()
            time2 = time.time()
            dtime = time2 - time1
            dtime = round(dtime)
            if dtime == 3:
                wrongAlertScreen = False
            screen.blit(tutorial_text, (120, 50))
            pygame.display.update()


    while scene_questroom:
        pygameQUIT()
        active_scene = img_scene_questroom
        screen.blit(img_scene_questroom, (0,0))
        characterMOVEMENT()
        victory()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_posx > -30 and player_posx < 110:
                        door_sound.play()
                        scene_questroom = False
                        scene_hallway = True
                        time.sleep(0.1)
                        player_posx = 870

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if player_posx > 175 and player_posx < 330:
                questscreen_lion = True
            if player_posx > 470 and player_posx < 630:
                questscreen_panda = True
            if player_posx > 755 and player_posx < 985:
                questscreen_monkey = True
            if player_posx == 1120:
                questscreen_cat = True

        font = pygame.font.Font('Assets/Font/bitfont.ttf', 20)
        text = font.render('QUEST completed: '+ str(quest_completed)+ '/4' , True, (0, 0, 0))
        screen.blit(text, (50, 30))

        mainQuest()
        pygame.display.update()
