class MyHashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [Bucket() for _ in range(size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        bucket_key = self._hash(key)
        return self.buckets[bucket_key].insert(key)

    def remove(self, key: int) -> None:
        bucket_key = self._hash(key)
        return self.buckets[bucket_key].delete(key)

    def contains(self, key: int) -> bool:
        bucket_key = self._hash(key)
        return self.buckets[bucket_key].exists(key)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Bucket:
    def __init__(self, val: int=None, next=None):
        self.head = Node(0)
    
    def insert(self, newVal):
        if not self.exists(newVal):
            newNode = Node(newVal, self.head.next)
            self.head.next = newNode
    
    def delete(self, value):
        prev, cur = self.head, self.head.next
        while cur:
            if cur.val == value:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
    
    def exists(self, value):
        cur = self.head.next
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)