# Program Phyton to find all even numbers
# Manual input
print("Program to find all even numbers, please type for start and end number")
#start, end = 4, 19

# Input by user
start = int(input("Enter the Start Number: "))
ends = int(input("Enter the End Number: "))

for x in range(start, ends + 1):
    # Checking condition
    if x % 2 == 0:
        print(x, end = " ")
        print(" ")


# Program Phyton to find all odd numbers
# Manual input

print("Program to find all odd numbers, please type for start and end number")
#starts, ends = 4, 19

# Input by user
startnum = int(input("Enter the Start Number: "))
endnum = int(input("Enter the End Number: "))

for z in range(startnum, endnum + 1):
    # Checking condition
    if z % 2 != 0:
        print(z, end = " ")
        print(" ")


