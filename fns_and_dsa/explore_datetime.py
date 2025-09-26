from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and prints the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.

    Args:
        current_date (datetime): The starting datetime object.
    """
    # Part 2: Calculate a Future Date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return

    # Create a timedelta object representing the duration
    time_difference = timedelta(days=days_to_add)

    # Calculate the future date by adding the timedelta
    future_date = current_date + time_difference
    
    # Format and print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    """
    Main function to execute the datetime operations.
    """
    # Execute Part 1 and store the result for Part 2
    current_date = display_current_datetime()
    
    # Execute Part 2
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
