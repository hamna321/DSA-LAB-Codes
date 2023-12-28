class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
    def display(self):
        for i in range(self.size):
            current = self.table[i]
            elements = []
            while current is not None:
                elements.append((current.key, current.value))
                current = current.next
            if elements:
                print(f"Slot {i}: {elements}")
# Example usage
hash_table = HashTable(10)
hash_table.insert(5, "Apple")
hash_table.insert(15, "Banana")
hash_table.insert(25, "Orange")
hash_table.insert(35, "Mango")
hash_table.display()