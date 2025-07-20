#Input task description

task = input("Enter the task description: ")

#Ask if its time bound
time_bound = input("Is the task time-bound? (yes/no): ").lower()

#Input task priority

priority = input("Enter the task priority (high, medium, low): ").lower()


#match case priority

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
   
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that needs to be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Complete when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still needs attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")
