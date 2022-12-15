# Import the date and time module
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Calculate the year, month, and day of the person's birth
birth_year = 1950
birth_month = 12
birth_day = 12

# Calculate the person's age
age = now.year - birth_year
if now.month < birth_month or (now.month == birth_month and now.day < birth_day):
    age -= 1

# Print the person's age
print("The person's age is:", age)
