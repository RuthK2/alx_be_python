task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high": 
       print(f"Reminder: '{task}' is a high priority task.", end="")
    case "medium":
       print(f"Reminder: '{task}' is a medium priority task.", end="")
    case "low":
       print(f"Reminder: '{task}' is a low priority task.", end="")

if time_bound == "yes":
  print(" This task requires immediate attention today!")
else:
 print(" Consider completing it when you have free time.")
 