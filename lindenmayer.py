from turtle import *
import time

"""
Angles move counter-clockwise, as with the unit circle:

       |
      90
       |
       | 
--180--+---0--
       |
       |
      270
       |

Rule set should be list of 2-tuples which are (before symbol, after string).
Constants should be list of 2-tuples which are (symbol, meaning).
Patterns should just be strings of symbols.

"""

#apply the rules one time to the provided pattern
def apply_rules(rules, pattern):
    new = []
    for char in pattern:
        applied = False
        for rule in rules:
            if char == rule[0]:
                new.append(rule[1]) #evolve char by appropriate rule
                applied = True
                break
        if applied == False: #char was not applicable for change, just append
            new.append(char)
    return "".join(new) #back to string


#evolve pattern to specific depth given provided starting pattern and rule set
#prints out evolved pattern at each step if verbose=True
def evolve_pattern(depth, pattern, rules, verbose=False):
    if verbose == True:
        print 0, " ", pattern
    for i in range(1, depth+1):
        pattern = apply_rules(rules, pattern) #evolve pattern
        if verbose == True:
            print i , " ", pattern
    return pattern
   

#draw the Lindenmayer system provided by the evolved pattern and constant meanings
#start_angle is rotated counter-clockwise, length is distance moved
def draw_pattern(angle, constants, pattern, length=1, start_angle=0, start_pos=(0,0), title="Lindenmayer System"):
    color("blue")
    up()
    goto(start_pos[0], start_pos[1])
    left(start_angle)
    down()
    
    farthest_left = start_pos[0]
    farthest_right = start_pos[0]
    highest = start_pos[1]
    direc = []
    direc.append(start_angle)
    posit = []
    posit.append((start_pos[0], start_pos[1]))
    
    beginning = time.time()
    
    for char in pattern:
        for con in constants:
            if char == con[0]:
                if con[1] == "forward": #draw forward
                    fd(length)
                    coords = pos()
                    farthest_left = min(coords[0], farthest_left)
                    farthest_right = max(coords[0], farthest_right)
                    highest = max(coords[1], highest)
                elif con[1] == "left": #turn left by angle
                    left(angle)
                elif con[1] == "right": #turn right by angle
                    right(angle)
                elif con[1] == "save": #save the current position and angle
                    posit.append(pos())
                    direc.append(heading())
                elif con[1] == "recall": #recall most recently saved pos/angle
                    up()
                    setx(posit[-1][0])
                    sety(posit[-1][1])
                    setheading(direc[-1])
                    down()
                    posit.pop()
                    direc.pop()
                elif con[1] == "move": #move forward without drawing
                    up()
                    fd(length)
                    down()
        
    end = time.time()
    print "Drawing time: %f sec" % (end-beginning)
    
    up()
    goto((farthest_left + farthest_right)/2, highest+25)
    color("red")
    write(title, align="center", font=("Arial", 14, "normal"))
        
        
if __name__ == "__main__":

    ht() #hide turtle cursor
    speed("fastest") #fastest animation
    
    
    
    
    rules = [("F", "F+F-F-F+F")] #rule set
    pattern = "F" #start pattern
    pattern = evolve_pattern(3, pattern, rules) #evolve pattern
    constants = [("+", "left"), ("-", "right"), ("F", "forward")] #meanings of constants
    draw_pattern(90, constants, pattern, length=15, title="Koch Curve") #animate L-system
    
    
    """
    rules = [("X", "X+YF"), ("Y", "FX-Y")]
    pattern = "FX"
    pattern = evolve_pattern(10, pattern, rules)
    constants = [("+", "right"), ("-", "left"), ("F", "forward")]
    draw_pattern(90, constants, pattern, length=10, start_angle=90, title="Dragon Curve")  
    
    
    rules = [("A", "B-A-B"), ("B", "A+B+A")]
    pattern = "A"
    pattern = evolve_pattern(8, pattern, rules)
    constants = [("+", "left"), ("-", "right"), ("A", "forward"), ("B", "forward")]
    draw_pattern(60, constants, pattern, title="Sierpinski Triangle")  
    
    
    rules = [("F", "FF"), ("X", "F-[[X]+X]+F[+FX]-X")]
    pattern = "X"
    pattern = evolve_pattern(6, pattern, rules)
    constants = [("+", "right"), ("-", "left"), ("F", "forward"), ("[", "save"), ("]", "recall")]
    draw_pattern(25, constants, pattern, length=2, start_pos=(-200,-200), start_angle=60, title="Fractal Plant")  
    """
    
    
    time.sleep(5)
    
        
    
