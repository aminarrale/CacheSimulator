from collections import Counter
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = Counter() # self.frequency[key] -> # of get or put functions calls
        # containing this key
        self.cache = {}
        self.t = 0
        self.time_by_key = {}
    # O(1)
    def get(self, key: int) -> int:
        self.t += 1
        if key in self.cache:
            self.frequency[key] += 1 
            self.time_by_key[key] = self.t
            return self.cache[key]
        return -1
    # Ideally O(1), but O(log n) should be passing
    # We could just get the O(n) idea out of the way
    # We have up to 2 * 10 ^ 5 calls (200000) calls to put function
    # if "# have to find least frequently used keys" takes 10^4 operations
    # the total number of operations (2 * 10 ^ 5) * 10 ^ 4 = 2 * 10 ^ 9
    def put(self, key: int, value: int) -> None:
        self.t += 1
        if key in self.cache: # O(1)
            self.time_by_key[key] = self.t 
            self.frequency[key] += 1 
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                # have to find least frequently used keys 
                min_frequency = min(self.frequency.values())
                lfu_keys = []
                for k in self.frequency.keys():
                    if self.frequency[k] == min_frequency:
                        lfu_keys.append(k)

                # if there's a tie, return least recently used key - this is O(1)
                min_time = self.time_by_key[lfu_keys[0]]
                worst_key = lfu_keys[0]

                for k in lfu_keys:
                    if self.time_by_key[k] < min_time:
                        min_time = self.time_by_key[k] 
                        worst_key = k 

                del self.cache[worst_key]
                del self.time_by_key[worst_key]
                del self.frequency[worst_key]

            self.time_by_key[key] = self.t 
            self.frequency[key] += 1 
            self.cache[key] = value

        # print(f"Cache: {self.cache}")
        # print(f"Time by key: {self.time_by_key}")
        # print(f"Frequency: {self.frequency}")
        # print("==============")
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)