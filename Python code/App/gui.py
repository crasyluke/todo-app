import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do") # This is a text instance with a string
input_box = sg.InputText(tooltip="Enter todo", key="todo") # Makes the key of this instance in the dictionary "todo"
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read() # Assigns "Add" to event and the dictionary to values
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED: # True when user closes the window
            break

window.close()