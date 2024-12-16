import datetime

# Set the last day of school (Year, Month, Day)
last_day_of_school = datetime.datetime(2025, 6, 11)

# Define multi-day breaks (as start and end dates) and individual holidays
breaks = [
    (datetime.date(2024, 12, 23), datetime.date(2025, 1, 3)),  # Christmas Break (2 weeks)
    (datetime.date(2025, 3, 31), datetime.date(2025, 4, 4)),  # Spring Break (1 week)
    (datetime.date(2024, 10, 18),),  # PD day Oct 18th (single day)
    (datetime.date(2024, 11, 11),),  # Veterans Day (single day)
    (datetime.date(2024, 11, 28),),  # Thanksgiving (single day)
    (datetime.date(2025, 1, 20),),   # MLK Day (single day)
    (datetime.date(2025, 1, 24),),   # Records Day (single day)
    (datetime.date(2025, 2, 7),),    # LID day FEB (single day)
    (datetime.date(2025, 2, 17),),   # Presidents Day (single day)
    (datetime.date(2025, 5, 26),),   # Memorial Day (single day)
]

# Function to check if a date is within a break or holiday
def is_in_break(date, breaks):
    for break_period in breaks:
        if len(break_period) == 1:  # Single-day holiday
            if date == break_period[0]:
                return True
        else:  # Multi-day break
            start, end = break_period
            if start <= date <= end:
                return True
    return False

# Function to calculate the countdown excluding weekends and breaks
def countdown_to_last_day():
    # Get the current date
    now = datetime.datetime.now()

    # Initialize the counter for weekdays
    weekdays_left = 0
    current_date = now.date()

    # Calculate the number of weekdays left
    while current_date <= last_day_of_school.date():
        # Check if the day is a weekday (Monday to Friday) and not in a break
        if current_date.weekday() < 5 and not is_in_break(current_date, breaks):
            weekdays_left += 1
        # Move to the next day
        current_date += datetime.timedelta(days=1)

    # Calculate remaining time to the last school day
    time_left = last_day_of_school - now

    # Break the difference into days, hours, minutes, and seconds
    days = time_left.days
    seconds_left = time_left.seconds
    hours = seconds_left // 3600
    minutes = (seconds_left % 3600) // 60
    seconds = seconds_left % 60

    # Print the countdown
    print(f"Countdown to the last day of school: {weekdays_left} weekdays (excluding holidays and breaks), {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Run the countdown function
countdown_to_last_day()
