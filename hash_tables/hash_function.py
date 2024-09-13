print(ord("a") - 96)

def hash(key, arrayLen):
    total = 0
    PRIME_NUMBER = 31
    min_range = min(len(key), 100)
    for index in range(min_range):
        value = ord(key[index]) - 96
        total = (total * PRIME_NUMBER + value) % arrayLen

    return total

print(hash("pink", 13))
print(hash("orange", 13))
print(hash("blue", 13))
print(hash("cyan", 13))
print(hash("purple", 13))
print(hash("hello", 13))
print(hash("goodbye", 13))
print(hash("hi", 13))
print(hash("cyan", 13))
