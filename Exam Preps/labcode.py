 # Cerating a open chaining close addressing method
def displayHashing(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for key, value in hashTable[i]:
            print("-->", end=" ")
            print(f"({key}, {value})", end=" ")
        print()
# creating hashtable for my value insertion
# empty list for adding value
HashTable = [[] for _ in range(10)]
# hashfuntions SHA-256
def hashingkey(keyvalue):
    return keyvalue % len(HashTable)
# inserting function for adding value
def insert(HashTable, keyvalue, value):
    hashkey = hashingkey(keyvalue)
    HashTable[hashkey].append((keyvalue, value))  
# creating function for searching the element
def search(HashTable, keyvalue):
    hashkey = hashingkey(keyvalue)
    for key, value in HashTable[hashkey]:
        if key == keyvalue:  
            return value
    return None
# creating delete for deleting the value
def delete(HashTable,Keyvalue):
    hashkey = hashingkey(Keyvalue)
    # enumerate help us when we want both value and index....
    for idx,(key,_) in enumerate(HashTable[hashkey]):
        if key == Keyvalue:
          HashTable[hashkey].pop(idx)
          print(f"Deleted = {Keyvalue}")
          return
    return(f"{Keyvalue} Not Found")
#adding value to me table
insert(HashTable, 4, 5)
insert(HashTable, 7, 8)
insert(HashTable, 8, 10)
insert(HashTable, 10, 4)
insert(HashTable, 2, 9)
insert(HashTable, 10, 7)

search_value = search(HashTable, 10)
print("Search Result:", search_value)

delete(HashTable, 8)
displayHashing(HashTable)



        