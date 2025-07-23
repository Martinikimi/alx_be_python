# Ask the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Start creating the reminder message
reminder = f"'{task}' is a {priority} priority task"

# Use Match Case to react differently based on the priority
match priority:
    case "high":
        reminder = f"Reminder: {reminder}"
    case "medium":
        reminder = f"Reminder: {reminder}"
    case "low":
        reminder = f"Note: {reminder}. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' priority is not recognized."

# Add extra message if the task is time-bound and high or medium priority
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"

# ✅ Simple loop (prints the reminder 3 times like a real reminder)
count = 1
while count <= 3:
    print(reminder)
    count += 1
