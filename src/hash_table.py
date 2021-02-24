class HashTable:
    def __init__(self, num_buckets=5):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def insert(self, key, value):
        self.buckets[self.hash_function(key)].append((key, value))

    def hash_function(self, string):
        return sum(ord(char)-97 for char in string) % self.num_buckets

    def find(self, key):
        return next((v for k, v in self.buckets[self.hash_function(key)] if k == key), None)

if __name__ == "__main__":
    ht = HashTable(num_buckets = 3)
    print(ht.buckets)
    # [[], [], []]
    print(ht.hash_function('cabbage'))
    # 2    (because 2+0+1+1+0+6+4 mod 3 = 14 mod 3 = 2)

    ht.insert('cabbage', 5)
    print(ht.buckets)
    # [[], [], [('cabbage',5)]]

    ht.insert('cab', 20)
    print(ht.buckets)
    # [[('cab', 20)], [], [('cabbage',5)]]

    ht.insert('c', 17)
    print(ht.buckets)
    # [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

    ht.insert('ac', 21)
    print(ht.buckets)
    # [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

    print(ht.find('cabbage'))
    # 5
    print(ht.find('cab'))
    # 20
    print(ht.find('c'))
    # 17
    print(ht.find('ac'))
    # 21
