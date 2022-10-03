# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pulsator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator, Mobile_Simulton):  
    
    def __init__(self, x, y, speed, angle):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self,x,y,self.radius*2,self.radius*2,angle,speed)
    
    
    def update(self):
        target = None
        # if len(model.find(Prey)) == 0:
        #     pass
        # else:
        for p in model.find(Prey):
            if self.distance(p.get_location()) < 200:
                if target == None: target = p
                elif self.distance(p.get_location()) < self.distance(target.get_location()): target = p
                    
        if target != None:
            y_dif = target.get_location()[1] - self.get_location()[1]
            x_dif = target.get_location()[0] - self.get_location()[0]
            self.set_angle(atan2(y_dif , x_dif))
            
            self.move()
            
        Pulsator.update(self)
