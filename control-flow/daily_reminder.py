task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""

match priority:
    case "high": 
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."

if time_bound == "yes":
    reminder += "This task requires immediate attention today!"
else:
    reminder += "Consider completing it when you have free time."

print(reminder)    