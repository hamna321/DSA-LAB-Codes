"write an algorithm for linear search algorithm"
arr = [1,2,3,4,5,6,7]
i = 0
val = 4
while i < len(arr):
    if arr[i] == val:
        print(arr[i])
        break
    else:
        i += 1
