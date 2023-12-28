# open chaining method 
def displayHashing(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for key, value in hashTable[i]:
            print("-->", end=" ")
            print(f"({key}, {value})", end=" ")
        print()

HashTable = [[] for _ in range(10)]

def hashingkey(keyvalue):
    return keyvalue % len(HashTable)

def insert(HashTable, keyvalue, value):
    hashkey = hashingkey(keyvalue)
    HashTable[hashkey].append((keyvalue, value))  # Modified to append a tuple

def search(HashTable, keyvalue):
    hashkey = hashingkey(keyvalue)
    for key, value in HashTable[hashkey]:
        if key == keyvalue:  # Compare key with keyvalue
            return value
    return None

def delete(HashTable,Keyvalue):
    hashkey = hashingkey(Keyvalue)
    for idx,(key,_) in enumerate(HashTable[hashkey]):
        if key == Keyvalue:
          HashTable[hashkey].pop(idx)
          print(f"Deleted = {Keyvalue}")
          return
    return(f"{Keyvalue} Not Found")

# Inserting values into the hash table
insert(HashTable, 4, 5)
insert(HashTable, 7, 8)
insert(HashTable, 8, 10)
insert(HashTable, 10, 4)
insert(HashTable, 2, 9)
insert(HashTable, 10, 7)

# Perform search and delete operations
search_value = search(HashTable, 10)
print("Search Result:", search_value)

delete(HashTable, 8)
displayHashing(HashTable)



        