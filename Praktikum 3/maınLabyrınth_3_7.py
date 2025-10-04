import gfx_stack
import playground_3_4
import xy_coordinates_3_5
from LabyrinthConversion_3_3 import labyrinth_conversion
import Wayfinder_3_6


def main():

    labyrinth_num = input("Which labyrinth you want to see? 1, 2 or 3?\t")
    direction = input("Which direction N S W E?\t")

    if (labyrinth_num=='1' and direction == 'N') or (labyrinth_num=='3' and direction == 'N'):
        print("This combination that you choose is not working, loop is occurring")
        exit()


    map_data = labyrinth_conversion(labyrinth_num)

    coordinates = xy_coordinates_3_5.find_start_goal(map_data)

    print("Start-Koordinaten:", coordinates["start"])
    print("Ziel-Koordinaten:", coordinates["goal"])

    positions = xy_coordinates_3_5.find_start_goal(map_data)
    start, goal = positions["start"], positions["goal"]

    gfx_stack.init_once(surface_resolution=(len(map_data[0]), len(map_data)))

    playground_3_4.draw_map(map_data)

    path = Wayfinder_3_6.move_avatar(map_data, start, goal, direction)


    if path:
        print("Avatar has arrived the end point!\n")

    gfx_stack.quit_prog()


if __name__ == "__main__":
    main()