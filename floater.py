# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    def __init__(self,x,y):
        self._width = 10
        self._height = 10
        self._speed = 5
        self._x = x
        self._y = y
        self._color = 'red'
        Prey.randomize_angle(self)
        Prey.__init__(self, x, y, self._width, self._height, self._angle, self._speed)
    def update(self, model):
        activate = False
        if random() < 0.3:
            activate = True
        if activate is True:
            speed_change = random() - 0.5
            angle_change = random() - 0.5
            if self._speed + speed_change < 3:
                self._speed -= speed_change
            elif self._speed + speed_change > 7:
                self._speed -= speed_change
            else:
                self._speed += speed_change
            self._angle += angle_change
        Prey.move(self)
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x + self._width/2, self._y + self._height/2, fill = self._color)
