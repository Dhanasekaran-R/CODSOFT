def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks,start=1):
            print(str(index)+"."+task)

def main():
    tasks=[]
    while True:
        print("\nOptions:")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Remove Task")
        print("4.Exit")

        choice=input("\nChoose an option: ")

        if choice=="1":
            task=input("Enter the task: ")
            tasks.append(task)
            print("Task added")

        elif choice=="2":
            show_tasks(tasks)

        elif choice=="3":
            show_tasks(tasks)

            try:
                task_num=int(input("Enter the number to remove: "))
                if 1<=task_num<=len(tasks):
                    removed_task=tasks.pop(task_num-1)
                    print("Removed: {removed_task}")

                else:
                    print("Invalid task number.")
                    
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice=="4":
            print("Goodbye")
            break

        else:
            print("Invalid option, please try again.")

if __name__=="__main__":
    main()








