class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = []

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def search(self, search_mode, search_value):
        results = []

        for key, value in self:
            if key[search_mode] == search_value:
                results.append(value)

        return results

    def __iter__(self):
        for bucket in self.table:
            if bucket is not None:
                for pair in bucket:
                    yield pair[0], pair[1]
