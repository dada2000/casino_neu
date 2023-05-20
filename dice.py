from random import randint
import functools
from collections.abc import Iterable

def parse_input(input_string): #Max 6 dice -> Converts str to int --> e.g. INPUT str(5) --> OUTPUT int(5)
    if input_string.strip() in [str(x) for x in range(1,7)]:
        return int(input_string)
    else:
        print("Entered number not within 1-6!")
        raise SystemExit(1)

def roll_dice(num_dice): #Random generator for num_dice --> returns list of dice results (int)
    return [randint(1,6) for _ in range(num_dice)]

#CALLING both initial 2x functions to create generate results...
num_dice_input = str(5)
#num_dice_input = input("How many dice [max. 6!]? [1-6]") #TOGGLE to get numc_dice input from CLI input()
num_dice = parse_input(num_dice_input) #Returns amount of dice as int() if <= 6
roll_results = roll_dice(num_dice) #Returns list with num_dice values as int #e.g. [4, 2, 2, 5, 1]

#Dictionary for dice_art { KEY[ int(1..6) ] : VALUE[ set("line1", ..., "line5") ] }
DICE_ART = {1:(
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    )}

def decorator(func): #Decorator function to check dice_values argument format type == list AND len(list) > 0.
    @functools.wraps(func)
    def inner_wrapper(args):
        #print(f"Rolled dice values:{args} --> len:{len(args)}")
        #print(f"func_name:{func.__name__} --> wrapper_name:{inner_wrapper.__name__}")
        if len(args) == 0:
            return f"!!! Entered empty dice value list: {args!r}"
        elif not isinstance(args, list):
            return f"!!! You did not enter a list: {args!r}"
        else:
            try:
                return func(args)   
            except Exception as message:
                return f"Exception raised for invalid dice value list: {args} " + str(message)
    return inner_wrapper
    #Preloads all required faces as tuples(5x strings) into dice_faces list
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value]) 
    #Stores all 5 ASCII rows for all dice into dice_faces_rows list
    dice_faces_rows = [] 
    for r in range(5): #Builds 1 complete line per iteration for all dice
        p_line = [] #Stores row components for each die in list
        for die in dice_faces: #Iterates through each die ASCII tuple (not line by line)
            p_line.append(die[r]) #Appends rth-line for all tuples to p_line
        row_string = " ".join(p_line) #Converts p_line list to str with " " separators
        dice_faces_rows.append(row_string) #Appends current line r for all dice to dice_faces_rows list. 
    #Creates results header string
    width = len(dice_faces_rows[0]) 
    #print("\n")
    diagram_header = f" RESULTS: {dice_values} ".center(width, "~")
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows) #Combines header and stored rows in multiline string
    return "\n" + dice_faces_diagram #Returns complete string output with ehader + faces

### START OF DECORATOR DEFINITION ###
@decorator
def generate_dice_faces_diagram(dice_values): #Combines DICE_ART string tuples for dice_values list.
    dice_art_tuples = [DICE_ART.get(k) for k in dice_values] #Stores string-tuples for dice_values in new list
    print("\n" + f" RESULTS FOR {dice_values} ".center(67,"="))
    for line in range(len(dice_art_tuples[0])):
        print("   ".join([i[line] for i in dice_art_tuples]))
    print("\n")
### END OF DECORATOR ###

generate_dice_faces_diagram(roll_results) #Calling main (decorator) function to print out dice values2

print("TEST")