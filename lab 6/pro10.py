''' write a code to show priority in queue.PriorityQueue Class method'''
from queue import PriorityQueue

pri_que = PriorityQueue()

# Insert elements with priority
pri_que.put((0, "Hamna"))
pri_que.put((4, "Minahil"))
pri_que.put((2, "Khadija"))
pri_que.put((3, "Laiba"))
pri_que.put((1, "Merub"))

# Print the elements in priority order
while not pri_que.empty():
    nxt_element = pri_que.get()
    print(nxt_element[1])  # Access the actual element, which is the second element in the tuple
