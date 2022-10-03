# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
# import model
# print(model.find)

class Ball(Prey): 
    radius = 5
    
    def __init__(self,x,y,speed,angle):
        Prey.__init__(self,x,y,Ball.radius*2,Ball.radius*2,angle,speed)    
    
    
    def update(self):
        self.move()
 
    # re-purposed from Pattis's program5helper 2022
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill='#0000ff')
