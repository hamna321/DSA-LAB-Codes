"Write a code that input value from user for ABC array and then remove it imediately.."
ABC = []
K =int(input("Enter the value for length:")) 
for i in range(K):
    M = int(input("Enter the value:"))
    ABC.append(M)
if len(ABC) > 2:
    ABC.pop(2)
print(ABC)
