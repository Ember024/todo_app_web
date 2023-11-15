FILEPATH = "todos.txt" #constant variables in modules are typically defined at the very top in all caps

def get_todos(filepath=FILEPATH): #defined default arguement for filepath
    """
     Read a text file and return the list of to-do items
     """  #Doc-String that explains the function via the help() function.
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local



def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__": # __name__ is a hidden variable already defined by python. __main__ reflects the current file
    print('Hello from functions')