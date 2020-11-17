class HashTable_LinearProbing(object):

    overflow_Count = 0

    def insert(self, key, value):

        for i in range(0, len(self)):
            hash_key = (key % len(self) + i) % len(self)
            if not self[hash_key] or self[hash_key] == "DELETED":
                self[hash_key].append((key, value))
                return
        HashTable_LinearProbing.overflow_Count += 1
        print("Overflow")

    def search(self, key):
        i = 0
        while self[i] != [] and i != len(self):
            j = (key % len(self) + i) % len(self)
            bucket = self[j]
            for v, kv in bucket:
                k = v
                if key == k:
                    return k, v
            i = i+1
        return "null"

    def delete(self, key):
        i = 0
        while i != len(self):
            j = (key % len(self) + i) % len(self)
            bucket = self[j]
            for v, kv in bucket:
                if key == v:
                    self[j] = []
                    return print("Key", key, "has been deleted")
            i = i+1
        return

    def getOverflow_Count(self):
        return HashTable_LinearProbing.overflow_Count
