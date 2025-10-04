import pygame
import gfx_stack
from LabyrinthConversion_3_3 import labyrinth_conversion

tile_colors = {  # Here we again created a dictionary data to access the colors of gfx_stack.py
    11:"Black",  # Walls (W)
    0: "White",  # Paths to use (.)
    1: "Viking", # Special numbers (1-9)
    2: "Viking",
    3: "Viking",
    4: "Viking",
    5: "Viking",
    6: "Viking",
    7: "Viking",
    8: "Viking",
    9: "Viking",
    22: "Golden Fizz",  # Starting pixel (S)
    33: "Brown",  # Ending pixel (Z)
}

def draw_map(map_data):
    # enumerate function returns both the row index and the row itself that is why y and x is indexes and row is row, tile is element
    for y, row in enumerate(map_data): # here y and x is indexes and row variable is the rows in map_data (we are iterating inside)
        for x, tile in enumerate(row): # and also tile variable is the column/element (we are iterating through all the elements in the present row)
            color_name = tile_colors.get(tile, "Dim Gray")  # chooses the color by looking the tile integer value and gets it
            #print(color_name)                              # and after since we get integer keys inside tile_colours dictionary we get colour names
                                                            # and if there is no such a value that integer will be coloured as "Dim Gray"
        # Note that we used get() function which is a function for dictionaries to search for the given key and get the value of it from tht dictionary data.
        # If there is no such a key in that dictionary, 2nd argument which is "Dim Gray" will be assigned as a colour for that unfounded key value
            gfx_stack.set_pixel((x, y), color_name) # it draws a coloured pixel with the color name that color_name variable holds as a color at the position (x,y).

    gfx_stack.event_loop()  # Refresh the window

def main():
    # Main function for loading and drawing the labyrinth.
    ltype = input("Which labyrinth you want to see? 1, 2 or 3?\t")

    map_data = labyrinth_conversion(ltype) # we got the normalized labyrinth list from LabyrinthConversion_3_3.py

    gfx_stack.init_once(surface_resolution=(len(map_data[0]), len(map_data))) # to fit all the maze to our window
    # which window's resolution is determined in the gfx_stack.init_once function

    draw_map(map_data) # we coloured with the numbers that are attached to specified pixel colours in the tile_colors dictionary.

    while not gfx_stack.stop_prog: # while we do not stop program (pushing the button 'q')
        gfx_stack.event_loop()     # we start the loop of event to see the map of labyrinth.

    gfx_stack.quit_prog() # if we don't enter the while loop to visualize the map of labyrinth, we quit the program.

if __name__ == "__main__":
    main()