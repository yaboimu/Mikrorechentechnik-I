import gfx_stack
from playground_3_4 import draw_map
import time
from LabyrinthConversion_3_3 import labyrinth_conversion
import xy_coordinates_3_5


AVATAR_COLOR = "Clairvoyant"
PATH_COLOR = "Twine"
speed = 0.0001 # Adjusting speed of the avatar and traces


DIRECTIONS = {    # direction dictionary to move avatar to that key value.
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

MOVE_ORDER = {    # Algorithm for the avatar movement respectively.
    "N": ["E", "N", "W", "S"], # Since we want from avatar to turn right of the direction that it is looking first,
    "E": ["S", "E", "N", "W"], # first element of the lists is adjusted like that. After, in our algorithm, if it is not
    "S": ["W", "S", "E", "N"], # possible to go right we want move through the direction that is looking so second element
    "W": ["N", "W", "S", "E"]  # in those lists is adjusted like that. Lastly, third and fourth element is adjusted like:
}                              # if the first two directions is not possible to move then check left side if it is not
                               # possible too then check backside of the direction that our avatar is looking.

def move_avatar(map_data, start, goal, direction):
    x, y = start
    path = [(x, y)] # path list to store all the coordinates that are visited (we will color them.)
    # and path variable is needed to check if we have moved true some real coordinates or None values.

# Important note: Here x,y is present coordinates; new_x,new_y is future coordinates; dx,dy is the movement coordinates

    while (x, y) != goal:   # when we are not reached to the ending/goal point program will continue to run.
        if gfx_stack.stop_prog:  # Check if 'q' was pressed
            print("Program ended.\n")
            return None

        #moved = False
        for new_dir in MOVE_ORDER[direction]: # direction here has been gotten from the user input (N, S, W, E)
        # and new_dir iterates inside of the key values of MOVE_ORDER direction
            dx, dy = DIRECTIONS[new_dir] # getting dx,dy to add our present x,y coordinates to make our avatar move.
            new_x, new_y = x + dx, y + dy # future coordinates where our avatar will move.


            if check_move(map_data, new_x, new_y):  # if condition statement for ensuring that our avatar cannot pass
                                                    # the borders of our maze map
                gfx_stack.set_pixel((x, y), PATH_COLOR) # we use x,y for the pos. to set pixel color since
                                            # we want to show where avatar has passed previously.

                x, y = new_x, new_y # we assign new coordinates to previous coordinates since we are now in that future
                                    # future coordinates which basically means our avatar has moved.
                direction = new_dir # we save the looking direction for our algorithm
                path.append((x, y))

                break

        gfx_stack.set_pixel((x, y), AVATAR_COLOR)  # Avatar's new position
        time.sleep(speed)
        gfx_stack.event_loop()
        # print(path) ----> in order to see what we get as a path list
    return path

def check_move(map_data, x, y):

    max_x = len(map_data[0]) # row length
    max_y = len(map_data) # column length

    if 0 <= x < max_x and 0 <= y < max_y:
        return map_data[y][x] not in [11]  # 11 = Wall
    else:
        return False

def main():

    # Ask for all user inputs BEFORE opening the window
    a = input("Which labyrinth you want to see? 1, 2 or 3?\t")
    direction = input("Which direction N S W E?\t")  # Ask for direction first

    if (a=='1' and direction == 'N') or (a=='3' and direction == 'N'):
        print("This combination that you choose is not working, loop is occurring")
        exit()

    map_data = labyrinth_conversion(a)  # Labyrinth laden
    positions = xy_coordinates_3_5.find_start_goal(map_data)
    start, goal = positions["start"], positions["goal"]

    # Now initialize graphics AFTER user input
    gfx_stack.init_once(surface_resolution=(len(map_data[0]), len(map_data)))
    draw_map(map_data)

    # Move avatar (pass direction as argument)
    maze_ = move_avatar(map_data, start, goal, direction) # when code reads this line it will go to the function move_avatar
    # and continue inside that function. After it will move on to line 97 then 101 respectively.

    if maze_: # here if path list data is empty or has None value inside of it, code will not enter to this if condition
        # move_avatar function returns None value (at the line 37) when user press 'q'
        print("Avatar has arrived the end point!\n")

    gfx_stack.quit_prog()

if __name__ == "__main__":
    main()