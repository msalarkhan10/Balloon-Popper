import pygame
import sys
import random
import time
from BalloonPop_helper import *

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
    
    def burst(self):
        global score
        posistion=pygame.mouse.get_pos()
        if onBalloon(self.x , self.y, 30,38 , posistion):
            score=score + 1
            self.reset()
        
    

balloons=[]
number_of_balloons = 30

for balloon in range(number_of_balloons):
    balloon_obj = Balloon(random.choice([1,2,2,6,7,1,9]))

   
balloons.append(balloon_obj)


clock=pygame.time.Clock()
black=(0,0,0)
scoreboard_background=(135,206,235)




def game_loop(): 
    global score   


    play_game = True

    while play_game:
        pygame.display.fill(black)
        for i in range(number_of_balloons):
            balloons[i].show()
            balloons[i].move()
            pygame.display.update
            clock.tick(60)

        for i in pygame.event.get():
            if pygame.event.type ==pygame.MOUSEBUTTONDOWN:
                for i in range(number_of_balloons):
                    balloons[i].burst()
            if pygame.event.type==pygame.QUIT:
                pygame.quit()
                sys.quit()

        pygame.draw.rect(pygame.display,scoreboard_background,(0,400,500,100))
        score_text=pygame.font.render("balloon_popped" + str(score) , True,black)
        pygame.display.blit(score_text,(200,400))

game_loop()        