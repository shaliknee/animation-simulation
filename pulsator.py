# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from special import Special
import model


class Pulsator(Black_Hole): 
    reset_threshold = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self._counter = 0


    def update(self):
        eaten = Black_Hole.update(self)
        if len(eaten) > 0:
            self._counter = 0
            for prey in eaten:
                if not isinstance(prey, Special):
                    self.set_dimension(self.get_dimension()[0] + 1, self.get_dimension()[1] + 1)
                    self.radius += 0.5
        else: self._counter += 1
        
        if self._counter == self.reset_threshold:
            self.set_dimension(self.get_dimension()[0] - 1, self.get_dimension()[1] - 1)
            self.radius -= 0.5
            self._counter = 0
            
        if self.get_dimension() == (0,0):
            model.remove(self)
        return eaten
