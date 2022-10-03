# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):  
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius*2, Black_Hole.radius*2)


    def update(self):
        eaten = set()
        for p in model.find(Prey):
            if self.contains(Simulton.get_location(p)):
                eaten.add(p)
                model.remove(p)
        return eaten


    def contains(self, xy):
        return True if Simulton.distance(self, xy) < self.radius else False

    # re-purposed from Pattis's program5helper 2022
    def display(self, canvas):
        canvas.create_oval(self._x-(self.get_dimension()[0] / 2), self._y-(self.get_dimension()[1] / 2),
                                self._x+(self.get_dimension()[0] / 2), self._y+(self.get_dimension()[1] / 2),
                                fill='#000000')
