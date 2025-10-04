filename = "Labyrinth-1.txt"
# this code is only for opening and reading the file that we choose
def labyrinth(filename):
    with open(filename, "r") as file:
        labyrinthFile = [list(line.strip()) for line in file] #.strip() takes space out before and after
        # a string with list() converts each line into a list
    """Printing Labyrinth row by row"""
    for row in labyrinthFile: # for each list of chars in labyrinthFile
        print(" ".join(str(chr) for chr in row)) # " " joins chars together in each row by converting
                                                # the chars to strings
    return labyrinthFile

def main():
    labyrinth(filename)

if __name__ == "_main_":
    main()