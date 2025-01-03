"""
d) According to the Gregorian calendar, it was Monday on the date 01/01/01. 
If any year is input through the keyboard write a program to find out what is the day on 1 January of this year.
"""
# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Start year and day for 01/01/01
start_year = 1
start_day_index = 0  # 0 for Monday

# Input year
year = int(input("Enter the year: "))

# Check if a year is a leap year
is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Number of days between 01/01/01 and the given year
total_days = 0

# For each year from 01 to the year before the given year, add days
while start_year < year:
    if is_leap_year(start_year):
        total_days += 366
    else:
        total_days += 365
    start_year += 1

# Find the day
day_index = (start_day_index + total_days) % 7

# Output the corresponding day
print(f"On 1st January {year}, it is a {days_of_week[day_index]}.")




To determine the day of the week for 1 January of any given year based on the Gregorian calendar, 
where 01/01/01 is a Monday, you can use the Zeller's 
Congruence formula or calculate the number of days passed since 01/01/01. 
Below is a Python solution based on the latter approach.



-----------------------------------

def find_day_of_january_1st(year):
    # Days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Start year and day for 01/01/01
    start_year = 1
    start_day_index = 0  # 0 for Monday

    # Function to check if a year is a leap year
    def is_leap_year(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    # Calculate total days between start_year and the given year
    total_days = 0
    for y in range(start_year, year):
        total_days += 366 if is_leap_year(y) else 365

    # Calculate the index of the day
    day_index = (start_day_index + total_days) % 7

    # Return the corresponding day
    return days_of_week[day_index]

# Input year
year = int(input("Enter the year: "))
day = find_day_of_january_1st(year)
print(f"On 1st January {year}, it is a {day}.")
