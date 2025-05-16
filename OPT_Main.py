#main file for OPT cache replacement 
import random
from optcache import OPTCache



# Generate 1000 random requests (digits 0–9)
requests = [random.randint(0, 9) for _ in range(1000)]

# Initialize cache
cache = OPTCache(capacity=4, future_accesses=requests) #you can change the cache size here
cache.process_requests()

print_steps = set(range(10)) | set(range(99, 1000, 100))

print("OPT Cache States:")
for i in print_steps:
    print(f"Request {i + 1}: Accessed {requests[i]}, Cache: {cache.states[i]}")

# Print stats
print("\nOPT Cache Performance:")
print(f"Total Requests: {len(requests)}")
print(f"Hits: {cache.hits}")
print(f"Misses: {cache.misses}")
print(f"Hit Ratio: {cache.hits / len(requests) * 100:.2f}%")
print(f"Miss Ratio: {cache.misses / len(requests) * 100:.2f}%")