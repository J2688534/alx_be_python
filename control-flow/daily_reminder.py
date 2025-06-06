# Step 1: Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"


# Step 3: Add time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

print(f"Reminder: '{task}' is a {priority} priority task{reminder}")
