num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print(largest)
