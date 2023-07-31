from function import get_todos,write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Now is "+now)
while True:
    user_action = input("Type add, show, edit, complete or exit:\n")
    user_action = user_action.strip()

    if  user_action.startswith('add'):
        
        # todo = input("Enter a to do:")+"\n"

        todo = user_action[4:]

        # 等同于with open的写法，这种写法要close，with open不用close
        # file = open('todo.txt','r')
        # td=file.readlines()
        # file.close()

        td=get_todos("todo.txt")

        td.append(todo+'\n')

        # file = open ('todo.txt','w')
        # file.writelines(td)
        # file.close()

        write_todos("todo.txt",td)

    elif user_action.startswith('show'):

        # file = open('todo.txt','r')
        # td=file.readlines()
        # file.close()

        td=get_todos("todo.txt")

        new_td = []

        for i in td:
            new_i = i.strip('\n')
            new_td.append(new_i)

        # new_td=[i.strip('\n') for i in td]  一种看上去很厉害的新写法

        for index, item in enumerate(new_td): #enumerate:print list 前面的序号。
            # print(index+1,'-',item) #常规print格式
            row = f"{index+1}-{item}"  # f string, 用于print 没有空格的格式
            print(row)
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            n =number- 1

            td=get_todos("todo.txt")

            new_todo = input("Enter new todo:\n")
            td[n] = new_todo + '\n'

            write_todos("todo.txt",td)
            
        except ValueError:
            print("Your command is not valid.")
            continue
        
    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])

            td=get_todos("todo.txt")

            rem = td[num-1].strip('\n')
            td.pop(num-1)

            write_todos("todo.txt",td)

            message = f"To do {rem} was remove from the list"
            print(message)
        except IndexError:
            print("not in list")
            continue
    else:
        print("your enter is not correct, please check")


print("Bye")
