# Коллизии возникают, когда у нескольких объектов одинаковый хеш.
# Для обработки таких ситуаций существуют методы разрешения коллизий.

# Метод цепочек использует связный список, хранящий в себе все объекты
# с одинаковым хешем


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[hash_key] is None:
            self.table[hash_key] = new_node
        else:
            current = self.table[hash_key]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        hash_key = self.hash_function(key)
        current = self.table[hash_key]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        hash_key = self.hash_function(key)
        current = self.table[hash_key]
        prev = None

        while current and current.key != key:
            prev = current
            current = current.next

        if current is None:
            return False

        if prev is None:
            self.table[hash_key] = current.next
        else:
            prev.next = current.next

        return True

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")


ht = HashTableChaining(10)
print("Количество бакетов для хешей равно 10 шт.")
ht.insert("foo", 1)
ht.insert("bar", 2)
ht.insert("baz", 3)
ht.display()

print("Поиск значения для элемента:", ht.search("baz"))

ht.delete("baz")
ht.display()


class HashTableLinProb:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_fuction(self, key):
        print(hash(key) % self.size)
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_fuction(key)
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.size
        self.table[hash_key] = key, value

    def search(self, key):
        hash_key = self.hash_fuction(key)
        while self.table[hash_key] is not None:
            if self.table[hash_key][0] == key:
                return self.table[hash_key][1]
            hash_key = (hash_key + 1) % self.size
        return None

    def delete(self, key):
        hash_key = self.hash_fuction(key)
        while self.table[hash_key] is not None:
            if self.table[hash_key][0] == key:
                self.table[hash_key] = None
                return True
            hash_key = (hash_key + 1) % self.size
        return False

    def display(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"Bucket {i}: None")
            else:
                print(f"Bucket {i}: {self.table[i]}")


ht = HashTableLinProb(3)
ht.insert("foo", 1)
ht.insert("bar", 2)
ht.insert("baz", 3)
ht.display()

print("Поиск значения для 'baz':", ht.search("baz"))

ht.delete("baz")
ht.display()
