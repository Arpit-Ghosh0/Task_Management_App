def task():
    tasks = [] #empty list
    print("----Lets Manage Your Task----") #Greeting the user

    total_task = int(input("Enter how many tasks you have today = "))   #asking the user total tasks
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name) #looping through the total_task and append in tasks 
    print(f"Today's tasks are\n{tasks}") #all tasks viewed
    while True:  #endless loop
        operation = int(input("Enter\n1- ADD\n2- Update\n3- Delete\n4- View\n5- Exit/Stop/"))
        if operation ==1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
        elif operation ==2:
            updated_val = input("Enter the task you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val) #getting the index for the task to update it
                tasks[ind] = up
                print(f"Updated task {up}")
        elif operation == 3:
            del_val = input("Which task you dont want to do ?")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        elif operation == 5:
            print("Closing the program...")
            break
        else:
            print("Invalid Input...")
task()