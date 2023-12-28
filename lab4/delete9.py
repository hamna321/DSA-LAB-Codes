"Write a code that input value from user for ABC array and then remove it imediately.."
#             <--- 1 Code --->
ABC = []
N =int(input("Enter the value for length:")) 
for i in range(N):
    M = int(input("Enter the value:"))
    ABC.append(M)
    print(ABC)
if len(ABC) > 0:
    ABC.pop()

"Write a code that remove value from the end of array named as ABC"
#             <--- 2 Code --->
ABC = [1,2,3,4]
ABC.pop()
print(ABC)