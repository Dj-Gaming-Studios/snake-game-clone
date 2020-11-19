#!/usr/bin/python

import pygame 
from food import Food
from constants import WIN_HEIGHT, WIN_WIDTH

def main():
    pygame.init()
    done = False
    myFood = Food(320,240)

    screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                myFood.gotoRandomPos()
        screen.fill((255,255,255))
        myFood.draw(screen)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()