import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple5")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")  # This is a text instance with a string
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # Makes the key of this instance in the dictionary "todo"
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',  # Creates a list box using the todos list in the file
                      enable_events=True, size=[45, 10]) # The list box is 45 characters wide and 10 rows high
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)  # Assigns "Add" to event and the dictionary to values, the window is updated every 200 msec to display the clock
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # The 0 gives only the string without the brackets
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # Accesses the list box in the window and updates it
            except IndexError:  # Occurs when the user doesn't select an item
                sg.Popup("Please select an item first.", font=("Helvetica", 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:  # True when user closes the window
            break

window.close()
