stack= []
for i in range(6):
    values=int(input())
    stack.append(values)
print(stack)
# want to add more values in existing stack use extend function
stack.extend([10,11,14,13,541])
print(stack)