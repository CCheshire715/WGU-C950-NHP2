# Creates the class for the Hash Table.
class HashTable:

    # Constructor. O(n)
    def __init__(self, initial_capacity=10):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts item into Hash Table and also updates the item if the key is already existing in the table. O(n)
    def insert_into_list(self, key, item):
        container = hash(key) % len(self.list)
        container_list = self.list[container]

        for i in container_list:
            if i[0] == key:
                i[1] = item
                return True

        k_v = [key, item]
        container_list.append(k_v)
        return True

    # Removes item from Hash Table by key if found. O(n)
    def remove(self, key):
        container = hash(key) % len(self.list)
        container_list = self.list[container]

        for i in container_list:
            if i[0] == key:
                container_list.remove([i[0], i[1]])

    # Searches for item in Hash Table by key. Returns None if the item is not found. O(n)
    def search_list(self, key):
        container = hash(key) % len(self.list)
        container_list = self.list[container]

        for i in container_list:
            if i[0] == key:
                return i[1]
        return None
