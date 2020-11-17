class HashTable_Chaining(object):
    chaning_Count = 0

    def insert(self, key, value):
        hash_key = key % len(self)
        key_exists = False
        if self[hash_key]:
            HashTable_Chaining.chaining_count(self)
        bucket = self[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def chaining_count(self):
        HashTable_Chaining.chaning_Count += 1

    def get_chaning_count(self):
        return HashTable_Chaining.chaning_Count

    def search(self, key):
        hash_key = key % len(self)
        bucket = self[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(hash_table, key):
        hash_key = hash(key) % len(hash_table)
        key_exists = False
        bucket = hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))
