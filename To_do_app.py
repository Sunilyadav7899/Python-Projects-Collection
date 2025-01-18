def to_do():
    tasks = [] # Empty list
    print("-----WELCOME TO THE TO-DO APP-----")

    total_task = int(input("How many tasks would you like to add initially? - "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter the name of task {i}: ").strip().lower()
        tasks.append(task_name)
    
    while True:
        print(f"\nOptions Menu:\nEnter 1- Add a New Task\nEnter 2- Update an Existing Task\nEnter 3- Delete a Task\nEnter 4- View All Tasks\nEnter 5- Exit/Stop the App\n")
        user_choice = int(input("Enter your choice (1-5): "))
        if user_choice == 1:  # Add a new task
            new_task = input("Enter the name of the new task: ").strip().lower() 
            tasks.append(new_task)
            print(f"Task '{new_task}' has been successfully added.")

        elif user_choice == 2: # Update an existing task
            task_to_update  = input("Enter the name of the task you want to update: ").strip().lower()
            if task_to_update  in tasks:
                updated_task = input(f"Enter the updated name for the task '{task_to_update}': ").strip().lower()
                ind = tasks.index(task_to_update)
                tasks[ind] = updated_task
                print(f"Task '{task_to_update}' has been updated to '{updated_task}'.")
            else:
                print(f"Task '{task_to_update}' not found in the list. Please check the name and try again.")

        elif user_choice == 3: # Delete a task
            task_to_delete  = input("Enter what task you want to delete: ").strip().lower()
            if task_to_delete in tasks:
                finding = tasks.index(task_to_delete )
                tasks.pop(finding)
                print(f"{task_to_delete } successfully removed")
            else:
                print(f"Task '{task_to_delete}' not found in the list. Please check the name and try again.")

        elif user_choice == 4:  # View all tasks
            print(f"\nYour current tasks are:")
            if tasks != []:
                for idx,i in enumerate(tasks, start=1):
                    print(f"{idx}. {i}")
            else:
                print("You have no tasks in your list.")

        elif user_choice == 5:  # Exit the app
            print(f"Thank you for using the To-Do App. Goodbye!\n")
            break

        else:
            print("Invalid Input. Please enter valid input.")


to_do()  # Calling the function