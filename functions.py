def get_todos(filepath="todos.txt"):
    """ Read a text file & return the list of todo items. """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        todos_local_cap = []
        for todo in todos_local:
           todos_local_cap.append(todo.title())
    return todos_local_cap

def write_todos(todos_arg, filepath="todos.txt"):
    """Write the todo items list in the text file."""
    with open(filepath, 'w') as file:
       file.writelines(todos_arg)

"""print(__name__)
if __name__ == "__main__":
    print("Hello from functions!")
    print(get_todos())
"""