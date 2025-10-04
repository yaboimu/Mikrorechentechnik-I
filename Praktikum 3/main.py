#!/usr/bin/env python3
# main

import gfx_stack as gfx
import kommandozeilen_argumente as cmdargs


def paint_smiley():
    "Simple demonstration for drawing pixels."
    "Color names can be found in the module gfx_stack.py."
    gfx.set_pixel((30,20), "Black")
    gfx.set_pixel((31,20), "Black")
    gfx.set_pixel((30,21), "Black")
    gfx.set_pixel((31,21), "Light Steel Blue")

    gfx.set_pixel((50,21), "Light Steel Blue")
    gfx.set_pixel((51,21), "Black")
    gfx.set_pixel((50,20), "Black")
    gfx.set_pixel((51,20), "Black")

    gfx.set_pixel((30,30), "Mandy")
    gfx.set_pixel((32,32), "Brown")
    gfx.set_pixel((34,33), "Brown")
    gfx.set_pixel((36,34), "Brown")
    gfx.set_pixel((38,35), "Brown")

    gfx.set_pixel((40,35), "Brown")

    gfx.set_pixel((42,35), "Brown")
    gfx.set_pixel((44,34), "Brown")
    gfx.set_pixel((46,33), "Brown")
    gfx.set_pixel((48,32), "Brown")
    gfx.set_pixel((50,30), "Mandy")


def main():
    """Example of a main function for the experiment."""

    cmdargs.demo()

    # Open graphics window
    # create an 80 x 60 pixel drawing area
    # Adjust the size of the drawing area to the size of the labyrinth!
    gfx.init_once((80, 64))


    # draw, update and wait for user input
    while not gfx.stop_prog:
        # draw the test image
        gfx.color_demo_paint_on_surface()

        # Example react to Space key
        if gfx.space_key == True:
            print("Leertaste registriert")
            # Draw smiley
            paint_smiley()

        gfx.event_loop()

    # tidy up
    gfx.quit_prog()

if __name__ == '__main__':
    main()


