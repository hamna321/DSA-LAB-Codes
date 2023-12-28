class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0                  

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
        self.count += 1

    def insert_middle(self, data):
        new_node = Node(data)
        new_node.link = None
        if self.head is None:
            self.head = new_node
        else:
            mid = self.count // 2
            temp = self.head
            c = 1
            while c < mid:
                temp = temp.link
                c += 1
            new_node.link = temp.link
            temp.link = new_node
        self.count += 1

    def insert_end(self, data):
        new_node = Node(data)
        new_node.link = None
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = new_node
        self.count += 1

    def delete(self, key):
        current = self.head
        prev = None
        found = False

        while current:
            if current.info == key:
                found = True
                break
            prev = current
            current = current.link

        if found:
            if prev is None:
                # Deleting the head node
                self.head = current.link
            else:
                prev.link = current.link
            self.count -= 1
        else:
            print(f"{key} not found in the list.")

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end="\t")
            current = current.link
        print()
        print("Value of count =", self.count)

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_beg(2)
    linked_list.insert_end(21)
    linked_list.insert_middle(3)
    linked_list.display()

    linked_list.delete(3)
    linked_list.display()
