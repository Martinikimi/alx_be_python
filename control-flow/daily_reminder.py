#!/usr/bin/python3
# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Base reminder message
reminder = "'" + task + "' is a " + priority + " priority task"

# React differently based on priority (using if-elif)
if priority == "high":
    reminder += ""
elif priority == "medium":
    reminder += ""
elif priority == "low":
    reminder += ""
else:
    reminder += " (priority not recognized)"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

# Print the customized reminder
print("\nReminder:", reminder)

