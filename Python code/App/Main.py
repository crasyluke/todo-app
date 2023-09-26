# from functions import get_todos, write_todos # Imports the functions from another file
import functions # This is better than the above if there are many functions. (Retreives functions as a module)
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # Gives part of string after 4 characters, eg.'add ' (called list slicing)

        todos = functions.get_todos()  # Function call

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]  # Does the above function in one line (list comprehension)

        for index, item in enumerate(new_todos):  # enumerate gives index and item
            item = item.strip('\n')  # This is the simplest solution to remove the extra break line
            print(f"{index + 1}-{item}")  # f allows us to print without spaces

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:  # Tries the above and if user receives a value error, the below occurs
            print("Your command is not valid.")
            continue  # Runs another cycle of the while loop

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
            
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid, try again.")

print("Bye!")
