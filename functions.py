FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH): #default parameter
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
        # file = open('todos.txt', 'r') # todos = file.readlines() # file.close()

def write_todos(todos_arg, filepath=FILEPATH): #need to know what to write
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        #doesn't return 'cause it's an action


if __name__ == "__main__":
    #value of name is 'main' only in functions.py, when I'm running it directly here
    #if it's executed in command_line_interface.py, name od this file will be functions
    print("hello!")
    print(get_todos())