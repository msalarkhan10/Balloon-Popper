import pygame
import sys
import random

pygame.init()

w=500
h=500
x = "Balloon Popping Game :D "
pygame.display.set_mode((w , h))
pygame.display.set_caption(x)


class Balloon:
    def __init__(self,speed):
        self.x=random.randrange(100,400)
        self.y=random.randrange(100,400)
        self.speed=speed