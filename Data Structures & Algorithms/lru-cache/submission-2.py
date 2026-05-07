from time import time

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.time = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time[key] = time()
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache or len(self.cache) + 1 <= self.capacity:
            self.cache[key] = value
            self.time[key] = time()
        else:
            to_delete = sorted(self.time.items(), key = lambda kv: kv[1])[0]
            del self.cache[to_delete[0]]
            del self.time[to_delete[0]]
            self.cache[key] = value
            self.time[key] = time()
        

            
