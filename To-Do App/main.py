# To-Do APP
def view():
    pass


def add():
    pass


def remove_task():
    pass


def main():
    running = True

    while running:
        print("Welcome to ** Daily Task Manager **")
        print("1. View Your Today Task")
        print("2. Add your task")
        print("3. Delete your task")
        print("4. Exit")

        option = input("Choose an option (From 1-4): ")

        if option == '1':
            view()
        elif option == '2':
            add()
        elif option == '3':
            remove_task()
        elif option == '4':
            running = False


if __name__ == '__main__':
    main()



