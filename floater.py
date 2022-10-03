# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 

# THIS FLOATER CLASS UTILIZES RED OVALS INSTEAD OF ufo.gif


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random



class Floater(Prey): 
    radius = 5
    def __init__(self,x,y,speed,angle):
        Prey.__init__(self,x,y,Floater.radius*2,Floater.radius*2,angle,speed)


    def  update(self): # the only Prey type that overrides the Prey.update() method
        changed = random.choice([True, True, True, False, False, False, False, False, False, False])
        
        if changed:
            while True: #change speed
                self.set_speed(self.get_speed() + (random.random() - 0.5))
                if 3 <= self.get_speed() <= 7: break
                
            self.set_angle(self.get_angle() + (random.random() - 0.5)) # change angle
    
        self.move() #from Prey/Mobile_Simulton
 
    # re-purposed from Pattis's program5helper 2022
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='#ff0000')
