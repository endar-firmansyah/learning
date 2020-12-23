#Python program conversion from km to mile distance

# Convertion from miles to Kilometers
print("Convertion from Miles to Kilometers")
mil = float(input("Enter value in Miles: "))
kilo = 1.60934

conv = mil * kilo

print(f"Converting result from Miles to km is: ", conv, "Kilometers")

#Convertion from Kilometers to Miles
print("Convertion from Kilometers to Miles")
km = float(input("Enter value in Kilometers: "))
miles = 0.621371

conv_km_miles = km * miles

print(f"Converting result from Miles to km is: ", conv_km_miles, "Miles")
