import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycles = 0
objects = set()
run = False
selected_object = None
coordinate = ()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global cycles, objects, run
    run = False
    cycles = 0
    objects = set()

#start running the simulation
def start ():
    global run
    run = True
    


#stop running the simulation (freezing it)
def stop ():
    global run
    run = False


#step just one update in the simulation
def step ():
    global run, cycles
    if run is True:
        cycles += 1
        for obj in objects:
            obj.move()
        run = False
    else:
        cycles += 1
        for obj in objects:
            obj.move()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_object
    selected_object = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selected_object, coordinate
    coordinate = (x,y)
    if selected_object == 'Ball':
        add(Ball(x,y))
    elif selected_object == 'Remove':
        temp = set()
        for obj in objects:
            if obj.contains(coordinate):
                temp.add(obj)
        for s in temp:
            objects.remove(s)
    elif selected_object == 'Floater':
        add(Floater(x,y))
    elif selected_object == 'Black_Hole':
        add(Black_Hole(x,y))
    elif selected_object == 'Pulsator':
        add(Pulsator(x,y))
    elif selected_object == 'Hunter':
        add(Hunter(x,y))
    elif selected_object == 'Special':
        pass


#add simulton s to the simulation
def add(s):
    global objects
    objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    #LIST(OBJECTS)???
    global objects
    objects.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global objects
    return_set = set()
    for obj in objects:
        if p(obj) is True:
            return_set.add(obj)
    return return_set


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycles, run
    if run is True:
        cycles += 1
        #for prey1 in find(lambda x: isinstance(x, Prey)):
            #prey1.update(model)
        remove_next = set()
        for obj in objects:
            try:
                obj.update(model)
                for devoured in obj.update(model):
                    remove_next.add(devoured)
            except:
                obj.update(model)
        for prey1 in remove_next:
            remove(prey1)
        

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for simulton in controller.the_canvas.find_all():
        controller.the_canvas.delete(simulton)
    for obj in objects:
        obj.display(controller.the_canvas)
    controller.the_progress.config(text = str(len(objects)) + " simultons/" + str(cycles) + " cycles")
