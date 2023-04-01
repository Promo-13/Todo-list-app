
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:

    # Getting input and stripping out the white space in it
    user_action = input("Type add , show , edit , complete or exit: ")
    user_action = user_action.strip()

    # Adding a task
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = function.get_todos()
        todos.append(todo.capitalize())
        function.write_todos(todos)

    # Displaying the pending tasks
    elif user_action.startswith("show"):
        todos = function.get_todos()
        for index, x in enumerate(todos):
            x = x.strip('\n')
            print(f"{index+1}.{x}")

    # Editing a task
    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])
            todos = function.get_todos()
            new_todo = input("Enter a new todo: ")
            todos[num-1] = new_todo + "\n"
            function.write_todos(todos)
        except ValueError:
            print("Your command is not valid ! ")
            continue

    # Completing a task(Removing)
    elif user_action.startswith("complete"):
        try:
            todos = function.get_todos()
            num = int(user_action[9:])
            todo = todos[num-1].strip('\n')
            todos.pop(num-1)
            function.write_todos(todos)
            print(f"Todo {todo} has been removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue

    # Exit from the loop
    elif user_action.startswith("exit"):
        break

    # Invalid command
    else:
        print("Hey, you have entered an invalid command!")

