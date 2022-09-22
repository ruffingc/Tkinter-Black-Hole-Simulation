# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import math


class Black_Hole(Simulton):  
    def __init__(self,x,y):
        self._width = 20
        self._height = 20
        self._radius = float(self._width / 2)
        self._x = x
        self._y = y
        self._color = 'black'
        Simulton.__init__(self, x, y, self._width, self._height)
        
    def contains(self, xy):
        return self._radius >= abs((abs((xy[0] - self._x)**2) + abs((xy[1] - self._y)))**(1/2))
    
    def update(self, model):
        eaten = set()
        for prey1 in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(prey1.get_location()):
                eaten.add(prey1)
        return eaten
        
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x + self._width/2, self._y + self._height/2, fill = self._color)
