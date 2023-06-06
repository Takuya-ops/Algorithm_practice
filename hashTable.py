import hashlib


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        self.table[index].append([key, value])


if __name__ == "__main__":
    hash_table = HashTable()
    # print(hash_table.hash("car"))
    hash_table.add("car", "Tesla")
    hash_table.add("car", "Toyota")
    hash_table.add("pc", "Mac")
    hash_table.add("sns", "Youtube")
    print(hash_table.table)
