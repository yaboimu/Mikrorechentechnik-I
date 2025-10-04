def chooseType(cInput):
    if cInput == '1':
        filename = "Labyrinth-1.txt"
    elif cInput == '2':
        filename = "Labyrinth-2.txt"
    elif cInput == '3':
        filename = "Labyrinth-3.txt"
    return filename

def load_labyrinth(filename):
    # load_labyrinth function is used for loading/reading the txt file
    with open(filename, "r") as file: # opens the file with the read mode
    # by using with, we close the file that we open after we read it already
        labyrinthList = [list(line.strip()) for line in file] # by the strip() function we split every
        # char and we list every line (row) that is in file which is our txt filename
        # print(labyrinthList) -----> check we just checked what we had here
    return labyrinthList # we returned the 2D list that we created from the txt file we choose
                         # and we did not print it yet properly

def print_labyrinth(labyrinthList):
    # This function is for printing the labyrinth that we returned in the load_labyrinth function
    for row in labyrinthList: # for every rows in the returned file
        print(" ".join(str(chr) for chr in row)) # here we by .join() function we separate all chr
        # in the rows of labyrinthFile in order to have a good visualization

def main():
    cInput = input("Which labyrinth you want to see? 1, 2 or 3?\t") # user choose the labyrinth
    filename = chooseType(cInput)  # here we get filename
    get_labyrinth = load_labyrinth(filename) # we loaded the labyrinth as a 2D List and assigned it to a variable
    print("Here is the labyrinth pattern:\n")
    print_labyrinth(get_labyrinth) # we use our print function for the specific labyrinth user chose

if __name__ == "__main__":
    main()