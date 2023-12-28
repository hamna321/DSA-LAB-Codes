'''Write a code that used to insert a value M location in array ABC having N elements.'''
N = int(input("Enter the number of values: "))
ABC = []
for i in range(N):
    pos = int(input("Enter value:"))
    ABC.append(pos)

print("Items Array:", ABC)
ABC.append(7)
print(ABC)

if len(ABC) >= 3:
    ABC.insert(3,8)
    print(ABC)