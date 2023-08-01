Filepath="todo.txt"

def get_todos(filepath=Filepath):
    with open(filepath, 'r') as file:
        td = file.readlines()
    return td


def write_todos(td,filepath=Filepath):
    with open(filepath, 'w') as file:
        file.writelines(td)
        