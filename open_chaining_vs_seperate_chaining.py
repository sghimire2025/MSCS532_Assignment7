import time
import random
import string
import pandas as pd
from collections import defaultdict

# Generate random string keys
def generate_keys(num_keys, length=8):
    return [''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) for _ in range(num_keys)]

# Hash table with Open Addressing (Linear Probing)
class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def insert(self, key):
        idx = hash(key) % self.size
        start_idx = idx
        while self.table[idx] is not None:
            self.collisions += 1
            idx = (idx + 1) % self.size
            if idx == start_idx:  # Full cycle
                break
        self.table[idx] = key

# Hash table with Separate Chaining
class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, key):
        idx = hash(key) % self.size
        if len(self.table[idx]) > 0:
            self.collisions += 1
        self.table[idx].append(key)

# Evaluate collision handling for each strategy
def evaluate_strategy(strategy_class, keys, table_size):
    start_time = time.time()
    table = strategy_class(table_size)
    for key in keys:
        table.insert(key)
    end_time = time.time()
    return table.collisions, end_time - start_time

# Run test at different load factors
results = []
load_factors = [0.3, 0.5, 0.7, 0.9]
table_size = 5000

for lf in load_factors:
    num_keys = int(table_size * lf)
    keys = generate_keys(num_keys)

    oa_coll, oa_time = evaluate_strategy(OpenAddressingHashTable, keys, table_size)
    sc_coll, sc_time = evaluate_strategy(SeparateChainingHashTable, keys, table_size)

    results.append(["Open Addressing", lf, oa_coll, oa_time])
    results.append(["Separate Chaining", lf, sc_coll, sc_time])

# Output results
df = pd.DataFrame(results, columns=["Method", "Load Factor", "Collisions", "Time Taken (s)"])
print(df)
