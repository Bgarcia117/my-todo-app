FILEPATH = 'todos.txt'
# This is a constant that can be easily changed when needed.

def get_todos(filepath=FILEPATH):
    """ Reads a text files and returns a list of the items in the file."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg, filepath=FILEPATH):
     """ Writes items to the text file."""
     with open(filepath, 'w') as file:
            file.writelines(todos_arg)

if __name__ == "__main__":
     print('hello')
     print(get_todos())
# If this file is ran directly, the code will be executed. If it is imported, it will be ignored.