class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


if __name__ == "__main__":
    hmap = HashMap(5)

    hmap.put("apple", 10)
    hmap.put("banana", 20)
    hmap.put("grape", 30)

    print("Get apple:", hmap.get("apple")) 
    print("Get banana:", hmap.get("banana")) 

    hmap.put("apple", 50)  
    print("Updated apple:", hmap.get("apple")) 

    hmap.remove("banana")
    print("Get banana after remove:", hmap.get("banana")) 

    print("\nFinal HashMap state:")
    hmap.display()
