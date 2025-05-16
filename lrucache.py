class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.time_by_key = {}
        self.capacity = capacity
        self.t = 0
        self.hits = 0
        self.misses = 0

    def get(self, key: int) -> int:
        self.t += 1
        if key in self.cache:
            self.time_by_key[key] = self.t
            self.hits += 1
            return self.cache[key]
        else:
            self.misses += 1
            return -1

    def put(self, key: int, value: int) -> None:
        self.t += 1
        if key in self.cache:
            self.cache[key] = value
            self.time_by_key[key] = self.t
        else:
            if len(self.cache) >= self.capacity:
                # Find LRU key
                lru_key = min(self.time_by_key, key=lambda k: self.time_by_key[k])
                del self.cache[lru_key]
                del self.time_by_key[lru_key]
            self.cache[key] = value
            self.time_by_key[key] = self.t
