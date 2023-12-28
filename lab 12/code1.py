class Node:
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

head = None

def insert(data):
    global head
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    head = new_node

def reverse_display():
    temp = head
    while temp.next is not None:
        temp = temp.next

    while temp is not None:
        print(temp.info, end="\t")
        temp = temp.prev
    print() 

insert(2)
insert(6)
insert(10)

reverse_display()
