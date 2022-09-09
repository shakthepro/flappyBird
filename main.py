from multiprocessing.resource_sharer import stop
from turtle import back
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
pipeimage = r"flappyBird\pipe.png"
background_image = r"flappyBird\background.jpg"
birdplayer_image = r"flappyBird\bird.png"
sealevel_image = r"flappyBird\base.jpg"
pressSpaceBar = r"flappyBird\backgroundSpaceBar.png"
zero = py.image.load(r'flappyBird\0.png').convert_alpha()
one = py.image.load(r'flappyBird\1.png').convert_alpha()
two = py.image.load(r'flappyBird\2.png').convert_alpha()
three = py.image.load(r'flappyBird\3.png').convert_alpha()
four = py.image.load(r'flappyBird\4.png').convert_alpha()
five = py.image.load(r'flappyBird\5.png').convert_alpha()
six = py.image.load(r'flappyBird\6.png').convert_alpha()
seven = py.image.load(r'flappyBird\7.png').convert_alpha()
eight = py.image.load(r'flappyBird\8.png').convert_alpha()
nine = py.image.load(r'flappyBird\9.png').convert_alpha()

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
    startingYPos = int(height/2)
    startingXPos = int(width/5)

    pass

def randomPipes():
    pass

while True:
    #starting position of bird

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
                game()

