# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    def __init__(self,x,y):
        self._width = 10
        self._height = 10
        self._speed = 5
        self._x = x
        self._y = y
        self._color = 'blue'
        Prey.randomize_angle(self)
        Prey.__init__(self, x, y, self._width, self._height, self._angle, self._speed)
    def update(self, model):
        Prey.move(self)
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x + self._width/2, self._y + self._height/2, fill = self._color)
