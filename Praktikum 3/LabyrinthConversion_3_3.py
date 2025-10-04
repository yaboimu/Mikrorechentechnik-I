from read_file_3_2 import load_labyrinth, chooseType

# Here we will normalize the map that we have by changing the chars to integers for both cases (types of labyrinths)
# and then we will use this normalized matrix or list to color them with the gfx_stack.py

def labyrinth_conversion(ltype):

    if ltype == "1" or ltype == "2":
        # since we want to use key-value relation between char and integer we created a dictionary for this purpose
        string_to_int = { # for the type 1 labyrinths:
            "W": 11, # W is assigned to 11 which represents 'Wall'
            ".": 0,  # . is assigned to 0 which represents 'Path'
            "1": 1,  # integers between 1-9 are considered as special pixels
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "S": 22,  # S is assigned to 22 which represents 'Starting Point'
            "Z": 33,  # Z is assigned to 33 which represents 'Ending Point'
        }
    else:
        string_to_int = { # for the type 2 labyrinth:
            "W": 0,   # W is assigned to 0 which represents 'Path'
            "X": 11,  # X is assigned to 11 which represents 'Wall'
            "1": 1,   # integers between 1-9 are considered as special pixels
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "S": 22,  # S is assigned to 22 which represents 'Starting Point'
            "Z": 33,  # Z is assigned to 33 which represents 'Ending Point'
        }

    labyrinth_list = load_labyrinth(chooseType(ltype))

    map_data = [
        [string_to_int[char] for char in line] for line in labyrinth_list # Here:
    ] # we loop through labyrinth_list we get every row in each iteration that is being iterated by line variable
      # and we loop through that line variable we get every char variable which holds every element of that row of labyrinth_list
      # and at the end we put the key value into our string_to_int dictionary and get the value of that specific key value in this dictionary
      # by the end of this process we have a list data which name is map_data which holds our normalized labyrinth data
    # print(map_data) ----> check what we have in here (it looks like the same list but normalized as labyrinth_List in the task 3.2)

    for row in map_data: # this loop is for obtaining a proper visualization of our labyrinth list data
        print(" ".join(str(chr) for chr in row)) # Note for ourselves: it was print(row) and it printed the labyrinth with brackets and commas
    return map_data

def main():
    ltype = input("Which labyrinth you want to see? 1, 2 or 3?\t") # ltype is the labyrinth number it is not the type of labyrinth
    # Since we have type 1 in labyrinth-1 and labyrinth-2 and type 2 in labyrinth-3 we used the if condition as like in
    # the fifth line
    labyrinth_conversion(ltype)

if __name__ == "__main__": # ensures that if we import our py files to other py file, imported py file's main function
                           # will not also be running. We just need to reach the functions inside of this imported py
                           # py file. We will have other main function that is running in our main py file.
                           # But if we just execute this py file here separately it will run this main function
    main()