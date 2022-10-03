import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from simulton import Simulton
from ball       import  Ball
from blackhole  import Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special    import Special


import random
from math import pi, sqrt, pow
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False 
cycle_count = 0
simultons = set()
selected_object = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls, simultons
    
    for s in set(simultons):
        remove(s)
    cycle_count = 0
    simultons       = set()
    selected_object = None
    running = False


#start running the simulation
def start ():
    global running 
    running  = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running
    global cycle_count
    running = False
    cycle_count += 1
    for s in set(simultons):
        s.update()


def random_angle():
    # between 0 and 2pi
    return random.random()*pi*2

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_object
    selected_object = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    #if selected_object = 
    
    if selected_object in ['Black_Hole', 'Pulsator']:
        eval(f'add( {selected_object}(x,y))')
    elif selected_object != 'Remove': # Ball, Floater, Hunter, Special
        eval(f'add( {selected_object}(x,y,5,random_angle()))')
    
    else:
        for s in simultons:
            h, k = Simulton.get_location(s)
            d = sqrt(pow((x-h), 2) + pow((y-k), 2))
            if d < 10:
                remove(s)
                break


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    found = set()
    for s in simultons:
        if isinstance(s, p):
            found.add(s)
    return found


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for s in set(simultons):
            s.update()

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
        
    if len(simultons) > 0:
        for s in simultons:
            s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")
