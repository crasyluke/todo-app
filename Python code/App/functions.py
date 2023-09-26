FILEPATH = "todos.txt" # All caps is good for constants

def get_todos(filepath=FILEPATH):  # Custom function
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:  # Benefit of with content manager is that you don't have to close the file
        todos_local = file_local.readlines()  # Creates list using file
    return todos_local  # Function definition


def write_todos(todos_local, filepath=FILEPATH):
    """ Write a to-do items list in the text file.""" # Use doc strings in every function, this can also be used to write multi-line strings outside functinos.
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

if __name__ == "__main__": # __name__ has a value of "__main__" when the program being run is this one
    print(get_todos())