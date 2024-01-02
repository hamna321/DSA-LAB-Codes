class Node(object):
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
        
class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def insert(self, prevnode, newnode):
        newnode.next = prevnode.next 
        prevnode.next = newnode
    
    def delete(self, prevnode, targetnode):
        prevnode.next = targetnode.next
        targetnode.next = None
           
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:  # Fix: Changed 'temp == key' to 'temp.data == key'
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    
    # Linking the nodes
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3

    # Creating a linked list with the head node
    linked_list = LinkedList(n1)

    # Traversing and printing the linked list
    linked_list.traverse()

    # Example of inserting a new node after n2
    new_node = Node(25)
    linked_list.insert(n2, new_node)

    # Traversing and printing the updated linked list after insertion
    print("After inserting a new node:")
    linked_list.traverse()

    # Example of deleting the node n3
    linked_list.delete(n2, n3)

    # Traversing and printing the updated linked list after deletion
    print("After deleting a node:")
    linked_list.traverse()

    # Example of searching for a node with data value 30
    search_result = linked_list.search(30)
    print("Search result for 30:", search_result)

    # Example of searching for a node with data value 50
    search_result = linked_list.search(50)
    print("Search result for 50:", search_result)
