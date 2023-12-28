'''Write a code that input array ABC value & then sum the value(sum = 0)'''
ABC = []
n = int(input("Enter value for ending range:"))
sum = 0
for i in range(n):
    element =int(input("Enter the values="))
    ABC.append(element)
    sum += element
    print(sum)
