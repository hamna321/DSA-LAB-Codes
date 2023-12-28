class Node:
    def _init_(self, data):
        self.info = data
        self.link = None

head = None
count = 0

def insert_beg(data):
    global head, count
    new_node = Node(data)
    new_node.link = head
    head = new_node
    count += 1

def insert_middle(data):
    global head, count
    new_node = Node(data)
    new_node.link = None

    if head is None:
        head = new_node
    else:
        mid = count // 2
        temp = head
        c = 1
        while c < mid:
            temp = temp.link
            c += 1
        new_node.link = temp.link
        temp.link = new_node
        count += 1

def insert_end(data):
    global head, count
    new_node = Node(data)
    new_node.link = None

    if head is None:
        head = new_node
    else:
        temp = head
        while temp.link is not None:
            temp = temp.link
        temp.link = new_node
        count += 1

def display():
    current = head
    while current is not None:
        print(current.info, end="\t")
        current = current.link
    print()
    print("Value of count =", count)

if __name__ == "_main_":
    insert_beg(2)
    insert_end(21)
    insert_middle(3)
    display()