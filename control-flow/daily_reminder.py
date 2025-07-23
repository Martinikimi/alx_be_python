

# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case statement to handle priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' has an unknown priority."

# If statement to modify reminder based on time-bound condition
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"

# Print final customized reminder
print(reminder)
