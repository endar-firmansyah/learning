# Python program to display calendar of the given month and year
# Importing calendar module
import calendar
yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))

# Display the calendar
print(calendar.month(yy, mm))

