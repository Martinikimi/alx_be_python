# Ask the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Base reminder (ALX expects "Reminder:" for all)
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Add extra message for time-sensitive tasks
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder += ". Consider completing it when you have free time."

# Print final reminder
print(reminder)
