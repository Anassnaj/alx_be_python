from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))  # Format and print

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))  # Get user input
    future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))  # Format and print

if __name__ == "__main__":
    display_current_datetime()  # Call the function to display current date and time
    calculate_future_date()  # Call the function to calculate the future date
