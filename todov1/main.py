
todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show | display':
            for item in todos:
                print(item)
        case 'edit':
            index = input("Enter index of item to be edited: ")
            new_todo = input("Enter new item: ")
            todos[int(index)-1] = new_todo
            print(todos)
        case 'exit':
            break
        case default:
            print("You entered an incorrect command")
print('Bye')

