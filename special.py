# A Special class object is Prey; it is derived from a Prey 
#   and then Mobile_Simulton base. It updates by moving with a 
#   more erratic velocity--having a faster speed and more dramatic 
#   angle. It is smaller than other Prey (Ball, Floater) and does
#   not change the size of any instance objects of the Pulsator class.
#   Specials are meant to be highly populated in the canvas as a
#   'distraction' because Hunters will chase after fast Specials despite 
#   the fact that eating them will not increase the Hunter's size, thus



from prey import Prey
from random import random, randint

class Special(Prey):  
    radius = 3
    def __init__(self, x, y, speed, angle):
        Prey.__init__(self, x, y,Special.radius * 2, self.radius * 2,  angle, speed)
        self.set_velocity(self.get_speed() + (random() + 6), self.get_angle() + (random() + 2)) # random, erratic velocity
        self._color = "%06x" % randint(0, 0xFFFFFF) # random color     
        
    def update(self):
        self.move()
        

    # re-purposed from Pattis's program5helper 2022
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill=f'#{self._color}')