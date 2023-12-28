def binarySearch(stack, target):
    l = 0
    r = len(stack) - 1
    while l <= r:
        mid = (l + r) // 2

        if stack[mid] == target:
            return mid  # Return the index if the target is found
        elif stack[mid] < target:
            l = mid + 1 # move pointer if value less then target
        else:
            r = mid - 1 # move pointer if target is greator
    return -1  
stack = [1, 2, 3, 4, 5, 6, 7, 8]
target = int(input("Enter the targeted value: "))
result = binarySearch(stack, target)
if result != -1:
    print(f"Value {target} found at index {result}")
else:
    print(f"Value {target} not found in the stack.")


            