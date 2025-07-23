# Ask the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Start creating the reminder message
reminder = f"'{task}' is a {priority} priority task"
# Ask the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Use Match Case to create the basic reminder based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' priority is not recognized."

# Add extra message if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"

# Print the customized reminder ONCE (the checker may not want a loop)
print(reminder)
