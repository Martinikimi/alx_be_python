
# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")

# Loop until a valid priority is given
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter high, medium, or low.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to process based on priority
match priority:
    case "high" | "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Note: '{task}' has an unknown priority.")
