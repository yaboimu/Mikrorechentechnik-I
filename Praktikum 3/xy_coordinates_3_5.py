from LabyrinthConversion_3_3 import labyrinth_conversion

def find_start_goal(map_data):

    start = None
    goal = None

    for y, row in enumerate(map_data):  # here again y and x are our indexes of column and row respectively
        for x, tile in enumerate(row):  # and we want to keep those values as coordinates by using if condition
            if tile == 22:              # with searching for the integers which is corresponds to our Starting and Ending point.
                start = (x, y)
            elif tile == 33:
                goal = (x, y)

    return {"start": start, "goal": goal} # dictionary that returns the key values by writing the keys "start" and "goal"

def main():

    a = input("Which labyrinth you want to see? 1, 2 or 3?\t")

    map_data = labyrinth_conversion(a)

    coordinates = find_start_goal(map_data)

    print("Start-Koordinaten:", coordinates["start"])
    print("Ziel-Koordinaten:", coordinates["goal"])

if __name__ == "__main__":
    main()