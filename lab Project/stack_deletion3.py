# Method 3
stack = [1,2,3,4,5,42]
def isempty(stack):
    return len(stack) == 0
# remove top most element from stack 
while not isempty(stack):
    stack.pop()
print(stack)