'''write a code that input value for array & insert in array "Temp" ...'''
#             <--- 1 Code --->
Temp = []
for i in range(4):
    N = int(input("Enter the values"))
    Temp.append(N)
print("The index is=",i,"and",N)


#             <--- 2 Code --->
Temps =[1,2,3,4,5,7]
Temps.insert(5,6)
print(Temps)