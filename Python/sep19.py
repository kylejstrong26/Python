# Problem 1 #

def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
        
        
        
# Problem 2 #

def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turnRight()
    move()
    turnRight()
    while front_is_clear():
        move()
    turn_left()

       
   
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
        
        
        
# Problem 3 #

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():     
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()   
