class MyHashSet:

    def __init__(self):
        self._data = {}
        

    def add(self, key: int) -> None:
        self._data[key] = key
        return None
        

    def remove(self, key: int) -> None:
        self._data.pop(key, None)
        return None
        

    def contains(self, key: int) -> bool:

        return True if self._data.get(key) else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)