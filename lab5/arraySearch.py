arr = [1,4,3,5,6,8,10,11,14,17]
target_value = 8
# arr = [1,3,4,5,6,8,10,11,14,17]
#        0 1 2 3 4 5 6 7 8 9 10
def search(arr,target_value):
    l = 0
    r = len(arr)-1
    arr.sort()
    while l < r:
      mid = (l+r) // 2
      if arr[mid] == target_value:
         print(mid)
      elif arr[mid] < target_value:
         r = mid - 1
      elif arr[mid] > target_value:
         l = mid + 1
      print("mid = ",mid)
      return mid
    return -1
search(arr,target_value)
    
        