from datetime import datetime

def display_current_datetime():
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return current_date, formatted_datetime

current_date, formatted_datetime = display_current_datetime()
print("Current date and time:", formatted_datetime)

display_current_datetime()

from datetime import datetime, timedelta
def calculate_future_date(days):
    current_date = datetime.now().date()
    future_date = current_date + timedelta(days=days)
    return future_date
days_input = int(input("Enter the number of days to add to the current date: "))
future_date = calculate_future_date(days_input)
print ("Future date:", future_date.strftime("%Y-%m-%d"))
