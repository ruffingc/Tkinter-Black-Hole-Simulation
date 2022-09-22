# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    def __init__(self,x,y):
        self.cycles = 30
        Black_Hole.__init__(self, x, y)
        
    def update(self, model):
        removing = Black_Hole.update(self, model)
        if len(removing) > 0:
            self._width += 1
            self._height += 1
            self.cycles = 30
        else:
            self.cycles -= 1
            if self.cycles == 0:
                self._width -= 1
                self._height -= 1
                self.cycles = 30
                if sum(self.get_dimension()) == 0:
                    removing.add(self)
            Black_Hole.set_dimension(self, self._width, self._height)
        return removing
    