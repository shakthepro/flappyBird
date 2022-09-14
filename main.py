import pygame as py
import random  
import sys
from sys import exit
from pygame.locals import * 
import time

black = [0,0,0]
height =  510
width = 600
transparent = (0, 0, 0, 0) #RGB, transparency
window = py.display.set_mode((width, height)) 

#images
pipeimage = r"flappyBird\images\pipe.png"
background_image = r"flappyBird\images\background.jpg"
birdplayer_image = r"flappyBird\images\bird.png"
sealevel_image = r"flappyBird\images\base.jpg"
pressSpaceBar = r"flappyBird\images\backgroundSpaceBar.png"
zero = py.image.load(r'flappyBird\images\0.png').convert_alpha()
one = py.image.load(r'flappyBird\images\1.png').convert_alpha()
two = py.image.load(r'flappyBird\images\2.png').convert_alpha()
three = py.image.load(r'flappyBird\images\3.png').convert_alpha()
four = py.image.load(r'flappyBird\images\4.png').convert_alpha()
five = py.image.load(r'flappyBird\images\5.png').convert_alpha()
six = py.image.load(r'flappyBird\images\6.png').convert_alpha()
seven = py.image.load(r'flappyBird\images\7.png').convert_alpha()
eight = py.image.load(r'flappyBird\images\8.png').convert_alpha()
nine = py.image.load(r'flappyBird\images\9.png').convert_alpha()

if __name__ == "__main__":
    py.init()
    py.display.set_caption('Flappy Bird!')   
    pipeImageUp = py.image.load(pipeimage).convert_alpha()
    pipeImageDown = py.transform.rotate(pipeImageUp, 180)
    background_image = py.image.load(background_image).convert_alpha()
    birdplayer_image = py.image.load(birdplayer_image).convert_alpha()
    sealevel_image = py.image.load(sealevel_image).convert_alpha()

def game():
    print("game started")
    score = 0
    ground = 0
    startingYPos = int(height/2)
    print(startingYPos)
    startingXPos = int(width/5)
    print(startingXPos)
    upperPipes = randomPipes()
    lowerPipes = randomPipes()

    birdplayer_imageRect = birdplayer_image.get_rect()
    sealevel_imagRect = sealevel_image.get_rect()
    background_imageRect = background_image.get_rect()

    window.blit(background_image,background_imageRect)
    window.blit(sealevel_image, (0,startingYPos))
    window.blit(birdplayer_image, (startingXPos, startingYPos-100))
    py.display.flip()

    bird_velocity_y = -9
    bird_Max_Vel_Y = 10
    bird_Min_Vel_Y = -8
    birdAccY = 1
    bird_flap_velocity = -8
    bird_flapped = False

    while True:
        for event in py.event.get():
            if event.type == K_UP or event.type == K_w:
                #move the bird up 10 pixels
                if startingYPos > 0:
                    bird_velocity_y = bird_flap_velocity
                    bird_flapped = True
                #birdplayer_imageRect.y = birdplayer_imageRect.y + 10

def randomPipes():
    pipeHeight = pipeImageUp.get_height()
    pipeWidth = pipeImageUp.get_width()
    seperation = width/4
    randomHeight = random.randint(0, height - sealevel_image.get_height())

    y2 = seperation + random.randrange(0, height - sealevel_image.get_height())
    pipeX = width + 10
    y1 = pipeHeight - y2 + seperation

    pipe = [
        # upper Pipe
        {'x': pipeX, 'y': -y1},
          # lower Pipe
        {'x': pipeX, 'y': y2}  
    ]
    return pipe

while True:
    #bring up screen telling user to click space bar too start
    startingScreen = py.image.load(pressSpaceBar)
    startingScreenRect = startingScreen.get_rect()
    window.blit(startingScreen, startingScreenRect)
    py.display.flip()

    while True:
        for event in py.event.get():
            #turns off game if escape button is clicked or game is exited
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
        
            #countinues game if space bar is clicked
            if event.type == KEYDOWN and event.key == K_SPACE:
                #fill in window to black
                window.fill(black)
                py.display.flip()

                #display loading screen for random amount of seconds from 1 to 3
                loading = py.image.load(r"flappyBird\images\loadingScreen.jpg")
                loadingRect = loading.get_rect()
                #wait for random time (to make the game seem to load)
                randomTime = random.randint(1,3)
                print("Wait time is "+ str(randomTime))
                window.blit(loading, loadingRect)
                py.display.flip()
                time.sleep(randomTime)
                pass
                game() 

