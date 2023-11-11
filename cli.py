import function
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's:" , now)

while True:
    User_action = input("Type add, show, edit,complete or exit: ")
    User_action = User_action.strip()

    if User_action.startswith("add"):
        todo = User_action[4:]

        todos = function.get_todos()

        todos.append(todo + "\n")

        function.write_todos(todos)

    elif User_action.startswith("show"):
        todos = function.get_todos()

        for index, item in enumerate(todos):
            itme = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)


    elif "edit" in User_action:
        number = int(User_action[5:])
        print(number)

        number = number - 1

        with open("todos.txt" , "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"
        

        with open("todos.txt" , "w") as file:
            file.writelines(todos)

    elif "complete" in User_action:
        number = int(User_action[9:])

        with open("todos.txt" , "r") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todo[index].strip("\n")
        todos.pop(index)


        with open("todos.txt" , "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)


    elif "exit" in User_action:
        break

    else:
        print("Command is not Valid.")


print("Bye!")


 