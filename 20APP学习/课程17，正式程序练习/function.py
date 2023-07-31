def get_todos(filepath):
    with open(filepath, 'r') as file:
        td = file.readlines()
    return td


def write_todos(filepath,td):
    with open(filepath, 'w') as file:
        file.writelines(td)