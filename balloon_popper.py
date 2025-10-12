import pygame
import sys
import random
import time


pygame.init()

w=500
h=500
x = "Balloon Popping Game :D "
game_window=pygame.display.set_mode((w , h))
pygame.display.set_caption(x)

colour_blue = (0,0,255)
colour_red  = (255,0,0)



class Balloon:
    def __init__(self,speed):
        self.x=random.randrange(100,400)
        self.y=random.randrange(100,400)
        self.speed=speed
        self.colour=random.choice([colour_blue , colour_red])


    def show(self):
        pygame.draw.ellipse(game_window,self.colour,(self.x , self.y,30,38))
        pygame.draw.ellipse(game_window,self.colour,(self.x+10 , self.y+30,10,10))


    def move(self):
        self.y=self.y-self.speed


        if(self.y<0):
            self.reset()

    def reset(self):
        self.x=random.randrange(100,400)
        self.y=480
        self.speed=self.speed+0.49


    
        