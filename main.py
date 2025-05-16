#main file for LRU and LFU files
import random
from lrucache import LRUCache
from lfucache import LFUCache

# Initialize cache with size 4
#Change 'LRUCache' to 'LFUCache' to switch between LRU and LFU
# can also change cache size
cache = LRUCache(4)

# Generates a thousand random access values between 0 and 9
access_sequence = [random.randint(0, 9) for _ in range(1000)]

print_steps = set(range(10)) | set(range(99, 1000, 100))  # Steps: 1–10, 100, 200, ..., 1000

#hits and misss
hits = 0
misses = 0

for i, key in enumerate(access_sequence):
    if key in cache.cache:
        hits += 1
    else:
        misses += 1
    cache.put(key, key)
    if i in print_steps:
        print(f"Request {i + 1}: Accessed {key}, Cache: {cache.cache}")

# Final stats
total = hits + misses
hit_ratio = hits / total
miss_ratio = misses / total

print("\nCache Performance")
print(f"Total Requests: {total}")
print(f"Hits: {hits}")
print(f"Misses: {misses}")
print(f"Hit Ratio: {hit_ratio:.2%}")
print(f"Miss Ratio: {miss_ratio:.2%}")


