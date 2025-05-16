class OPTCache:
    def __init__(self, capacity: int, future_accesses: list):
        self.capacity = capacity
        self.cache = set()
        self.future_accesses = future_accesses
        self.hits = 0
        self.misses = 0
        self.states = []

    def process_requests(self):
        for i, key in enumerate(self.future_accesses):
            if key in self.cache:
                self.hits += 1
            else:
                self.misses += 1
                if len(self.cache) < self.capacity:
                    self.cache.add(key)
                else:
                    # Decide which key to evict
                    future_slice = self.future_accesses[i+1:]
                    next_use = {k: future_slice.index(k) if k in future_slice else float('inf') for k in self.cache}
                    key_to_evict = max(next_use, key=lambda k: next_use[k])
                    self.cache.remove(key_to_evict)
                    self.cache.add(key)
            self.states.append(self.cache.copy())
