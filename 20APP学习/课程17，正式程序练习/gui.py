import function
import PySimpleGUI 
import time

PySimpleGUI.theme("DarkPurple6")

clock=PySimpleGUI.Text('',key='clock')
label=PySimpleGUI.Text("Type in a to-do")
input_box=PySimpleGUI.InputText(tooltip="Enter to do",key="todo")

add_button = PySimpleGUI.Button("ADD")
list_box=PySimpleGUI.Listbox(values=function.get_todos(),key='todos',
                             enable_events=True,size=[45,10])
edit_button=PySimpleGUI.Button("EDIT")
complete_button=PySimpleGUI.Button("Complete")

exit_button= PySimpleGUI.Button("EXIT")

window=PySimpleGUI.Window('My To - Do App',
                          layout=[[clock],
                                  [label],
                                  [input_box,add_button],
                                  [list_box,edit_button,complete_button],
                                  [exit_button]], 
                          font=('Helvetiva',20))


while True:
    event,values=window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "ADD":
            todos=function.get_todos()
            new_todo= values['todo']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "EDIT":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo']
                
                new_todo2=new_todo.replace("\n","")
                new_todo3=new_todo2+"\n"
                # print(new_todo3)
                
                todos=function.get_todos()
                index=todos.index(todo_edit)
                todos[index]=new_todo3
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Select a item first",font=("Helvetica",20))
            # except ValueError:
            #     print("BUG")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_c=values['todos'][0]
                todos=function.get_todos()
                todos.remove(todo_c)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')  
            except IndexError:
                  PySimpleGUI.popup("Select a item first",font=("Helvetica",20))
        case "EXIT":
            break
        case PySimpleGUI.WIN_CLOSED:
            break
window.close()