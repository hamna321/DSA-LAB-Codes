from queue import Queue

que = Queue()
if que.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")
que.put(10)
que.put(20)
que.put(30)
que.put(40)
que.put(50)
print("Size of the queue:", que.qsize())
while not que.empty():
    item = que.get()  
    print(item, end=" ")
