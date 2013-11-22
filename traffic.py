import pygame
import sys
import math
from pygame import *
from pygame.locals import *
from pygame.sprite import *





#initialize pygame
pygame.init()



WIDTH=1300
HEIGHT=400
CAPTION = 'Traffic lights'
SPEED=0

MAX_SPEED=30
velocity=[10,10]


#make a class of cars
class Cars(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image=image.load('img/car.png')
        self.x=int(x) #variable denoting x position of car
        self.y=int(y) # y position of car
        self.rect=self.image.get_rect(center = (x,y)) #used to place the car

    def move(self,xp,sgn,a):
        
        xp=self.x+xp #new place for the car
        
        if xp>1200:
            xp = xp - 1200
        dista=xp-a.x
       
        if sgn == 0 or sgn == 1:
            self.rect.left=xp #move the car
            self.x=xp #update the car position
        elif sgn == 2:
            if self.x>700:
                self.rect.left=xp
                self.x=xp
            elif self.x>=700 and self.x<=750:
                pass
            elif dista>-200 and dista<200: #to check nearby cars
                pass
            else :
                self.rect.left=xp
                self.x=xp


class Signal(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('img/green.png')
        self.rect=self.image.get_rect(center=(700,50))
    def change_sign(self,color):
            self.image=image.load(color)





def traffic():

    clock = pygame.time.Clock() # load clock

    
    frame = pygame.display.set_mode((WIDTH, HEIGHT))
    display.set_caption(CAPTION)
    xp=100; 
    car1=Cars(xp+0,200)
    car2=Cars(xp+200,200)
    car3=Cars(xp+420,200)
    car4=Cars(xp+600,200)
    signal1=Signal()
    all_cars=Group(car1,car2,car3,car4)
    all_signals=Group(signal1)
    
    
    
    signal_list=['img/green.png','img/yellow.png','img/red.png'];

    signal_counter=0;
    
    
    
    while True:
        
        xp = 2
        car1.move(xp,signal_counter,car2)
        car2.move(xp,signal_counter,car3)
        car3.move(xp,signal_counter,car4)
        car4.move(xp,signal_counter,car1)
        e=event.wait()
        if e.type==KEYDOWN:
          if e.key==K_ESCAPE:
              break
        if e.type==MOUSEBUTTONDOWN:
            signal_counter+=1
            if signal_counter>2:
                signal_counter=0 
            signal1.change_sign(signal_list[signal_counter])
        
        
               
        frame.fill((255,255,255))
        all_cars.draw(frame)
        all_signals.draw(frame)
        display.update()
        pygame.display.flip()
    pygame.quit()

    clock = pygame.time.Clock() # load clock





if __name__ =='__main__':
    traffic()
