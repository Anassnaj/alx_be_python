# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Generate a reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level. Please enter high, medium, or low."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes" and "Invalid" not in reminder:
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and "Invalid" not in reminder:
        reminder += ". Consider completing it when you have free time."

    # Output the reminder
    print(reminder)

if __name__ == "__main__":
    main()

