tasks = []

while True:
    ch = input("\n1.Add  2.View  3.Exit: ")
    if ch == '1':
        tasks.append(input("Enter task: "))
    elif ch == '2':
        print("\nTasks:", *tasks or ["No tasks!"], sep="\n")
    elif ch == '3':
        break
    else:
        print("Invalid choice!")
