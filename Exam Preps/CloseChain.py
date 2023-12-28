class ClosedAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the table as a list of empty lists

    def hash_function(self, key):
        return key % self.size  # Modulus hashing function for simplicity

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:  # Update value if key already exists
                bucket[i] = (key, value)
                return

        bucket.append((key, value))  # Append new key-value pair to the bucket

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v  # Return value if key is found

        return None  # Return None if key is not found

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Delete key-value pair if key is found
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage
hash_table = ClosedAddressingHashTable(10)  # Initialize hash table with size 10

# Insert elements
hash_table.insert(5, 'Five')
hash_table.insert(15, 'Fifteen')
hash_table.insert(25, 'Twenty-Five')
hash_table.insert(10, 'Ten')
hash_table.insert(20, 'Twenty')

# Display hash table
hash_table.display()

# Perform search and delete operations
print("Search Result for key 25:", hash_table.search(25))

hash_table.delete(15)
print("After Deletion:")
hash_table.display()
