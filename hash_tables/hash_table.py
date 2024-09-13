class HashTable:
    def __init__(self, size):
        self.key_map = [None] * size

    def hash(self, key):
        total = 0
        WEIRD_PRIME = 31
        min_char = min(len(key), 100)

        for index in range(min_char):
            value = ord(key[index]) - 96
            total = (total * WEIRD_PRIME + value) % len(self.key_map)
        return total

    def set(self, key, value):
        index = self.hash(key)

        if self.key_map[index] is None:
            self.key_map[index] = []

        self.key_map[index].append([key, value])
        return

    def get(self, key):
        index = self.hash(key)

        if self.key_map[index] is not None:
            for pair in self.key_map[index]:
                if pair[0] == key:
                    return pair[1]
                return None

    def values(self):
        values_array = []
        for item in self.key_map:
            if item is not None:
                for pair in item:
                    if pair[1] not in values_array:
                        values_array.append(pair[1])
        return values_array


    def keys(self):
        keys_array = []
        for item in self.key_map:
            if item is not None:
                for pair in item:
                    if pair[0] not in keys_array:
                        keys_array.append(pair[0])
        return keys_array





hash_map = HashTable(13)

#hash_map.set("purple", "color")
hash_map.set("dog", "pet")
hash_map.set("read", "hobbie")
hash_map.set("apple", "food")
hash_map.set("pink", "color")
hash_map.set("cyan", "color")
hash_map.set("hello", "color")
hash_map.set("goodbye", "color")
hash_map.set("hi", "color")
hash_map.set("hello", "color")
hash_map.set("goodbye", "color")


print(hash_map.key_map)

print(hash_map.get("purple"))

print(hash_map.values())
print(hash_map.keys())
