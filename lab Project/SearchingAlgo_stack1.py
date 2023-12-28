# linear Search Algorithm on stack
stack = []
# for creating stack
for i in range(8):
    val = int(input("Enter the value:"))
    stack.append(val)
print(stack)
# to find specific value for linear search
target = int(input("Enter the value to search: "))
found = False

for i in range(len(stack)):
    if stack[i] == target:
        print(f"Value {target} found at index {i}")
        found = True
        break

if not found:
    print(f"Value {target} not found in the stack.")

    
    