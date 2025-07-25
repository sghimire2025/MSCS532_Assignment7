import time
import random
import string
import hashlib
from collections import defaultdict
import pandas as pd

# Generate random string keys
def generate_keys(num_keys, length=10):
    return [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(num_keys)]

# Bad hash function: only uses the first character's ASCII value
def bad_hash(key, table_size):
    return ord(key[0]) % table_size

# Good hash function: uses Python's built-in hash function
def good_hash(key, table_size):
    return hash(key) % table_size

# Very good hash function: uses SHA-256 for consistent hashing
def sha256_hash(key, table_size):
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % table_size

# Function to measure collisions and unique slot usage
def measure_collisions(hash_func, keys, table_size):
    table = defaultdict(int)
    for key in keys:
        index = hash_func(key, table_size)
        table[index] += 1
    collisions = sum(count - 1 for count in table.values() if count > 1)
    return collisions, len(table)

# Test parameters
num_keys = 10000
table_size = 5000
keys = generate_keys(num_keys)

# Test different hash functions
hash_functions = {
    "Bad Hash (First Char)": bad_hash,
    "Good Hash (Built-in)": good_hash,
    "Very Good Hash (SHA-256)": sha256_hash
}

# Evaluate and collect results
results = []
for name, func in hash_functions.items():
    start = time.time()
    collisions, unique_slots = measure_collisions(func, keys, table_size)
    end = time.time()
    results.append((name, collisions, unique_slots, end - start))

# Display results in a DataFrame
df = pd.DataFrame(results, columns=["Hash Function", "Collisions", "Unique Slots Used", "Time Taken (s)"])
print(df)
