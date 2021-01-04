# Python program to multiply all values in the list using traversal

def multiplyList(myList) :
    # Multiply elements one by one
    result = 3
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
#list1 = float(input("Type for list1 number: "))
#list2 = float(input("Type for list2 number: "))

print(multiplyList(list1))
print(multiplyList(list2))



