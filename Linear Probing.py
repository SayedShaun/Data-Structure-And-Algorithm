class Dictionary:
    def __init__(self, size):
        self.size = size
        self.key_slot = [None] * size
        self.value_slot = [None] * size

    def hash_function(self, key):
        return abs(hash(key) % self.size)

    def rehash_function(self, old_value):
        return (old_value + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.key_slot[hash_value] is None:
            self.key_slot[hash_value] = key
            self.value_slot[hash_value] = value
        else:
            new_hash_value = self.rehash_function(hash_value)
            while self.key_slot[new_hash_value] is not None and self.key_slot[new_hash_value] != key:
                new_hash_value = self.rehash_function(new_hash_value)

            if self.key_slot[new_hash_value] is None:
                self.key_slot[new_hash_value] = key
                self.value_slot[new_hash_value] = value
            else:
                self.value_slot[new_hash_value] = value

    def __setitem__(self, key, value):
        return self.put(key, value)

    def get(self, key):
        hash_value = self.hash_function(key)

        if self.key_slot[hash_value] == key:
            return self.value_slot[hash_value]

        new_hash_value = self.rehash_function(hash_value)
        while self.key_slot[new_hash_value] is not None and new_hash_value != hash_value:
            if self.key_slot[new_hash_value] == key:
                return self.value_slot[new_hash_value]
            new_hash_value = self.rehash_function(new_hash_value)

        return "Not Found"

    def __getitem__(self, item):
        return self.get(item)

    def print(self):
        print(self.key_slot)
        print(self.value_slot)


D = Dictionary(3)

D.put("shaun", "A Student")
D.put("rahim", "A Teacher")
D["John"] = "A boy"

print(D["shaun"])
print(D["John"])
print(D["F"])

D.print()
