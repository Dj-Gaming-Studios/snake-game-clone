import pygame
import random
from constants import WIN_WIDTH, WIN_HEIGHT

class Food:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.r = 10

  def gotoRandomPos(self):
    newX = random.randint(self.r,WIN_WIDTH - self.r)
    newY = random.randint(self.r,WIN_HEIGHT - self.r)

    self.x = newX
    self.y = newY

  
  def draw(self,screen):
    pygame.draw.circle(screen,(255,0,0),(self.x,self.y),self.r)