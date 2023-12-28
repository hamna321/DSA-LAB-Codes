def fb(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    else:
        return fb(n-1) + fb(n-2) 

result=fb(5)
print(result)