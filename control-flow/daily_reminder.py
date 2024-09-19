# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = "high priority task"
    case "medium":
        reminder = "medium priority task"
    case "low":
        reminder = "low priority task"
    case _:
        reminder = "task with unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + task + " is a " + reminder + ". Consider completing it when you have free time."

# Provide a Customized Reminder
print("Reminder: '{}' is a {}.".format(task, reminder))
