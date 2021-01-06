# Python program to find largest number in a list

# List of numbers
list = [13, 10, 25, 31, 56, 80, 95, 110, 250, -2, -7]

# Sorting the list
list.sort()

# Printing numbers in the list
print("The Numbers from the list is: ", list)

# Printing the first largest number in the list
print("The first largest number is:", list[-1])


# Printing the second largest number in the list
print("The second largest number is:", list[-2])

# Printing the last largest number in the list
print("The smallest number is:", list[0])

# Using list comprehension
# Print even number from list
even_num = [num for num in list if num % 2 == 0]
print("Even number from list is: ", even_num)

# Using list comprehension
# Print Odd number from list
odd_num = [oddnum for oddnum in list if oddnum % 2 == 1]
print("Odd number from list is: ", odd_num)




