'''Write an alogrithm for binary search Algorithm..'''
arr =[1,2,3,4,5,6,7,8,9]
target = 4
def binarysearch(arr,target):
    l = 0
    r = len(arr)-1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
           print(arr[l])
        elif arr[mid] < target:
            r = mid -1
        elif arr[mid] > target:
            l = mid + 1
        print("mid=",mid)
        return mid
    return -1 
binarysearch(arr,target)      