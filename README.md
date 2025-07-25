
# Hash Tables: Exploring Hash Functions and Collision Resolution

##  Overview

This project demonstrates how the design of **hash functions** and the choice of **collision resolution strategies** impact hash table performance. It includes Python implementations and performance analysis for:

- **Hash functions:** Bad (ASCII-based), Built-in, and SHA-256
- **Collision strategies:** Open Addressing and Separate Chaining

---
## Project Structure

This repository contains the code and documentation for **Assignment 7** of the MSCS532 course. It includes Python implementations and performance evaluations of hash functions and collision handling strategies in hash tables.

### Files:

- `hashing.py`  
  Contains the implementation and comparison of three types of hash functions: bad, built-in, and SHA-256. Measures performance metrics like collisions and unique slots used.

- `open_chaining_vs_open_addressing.py`  
  Implements and compares open addressing and separate chaining collision handling strategies. Analyzes collision count and execution time across various load factors.

- `README.md`  
  This file. Provides an overview of the project structure, usage instructions, and experiment summary.

- `MSCS532_Assignment7.docs`
    This file containe the documentation about the hashing function, its implementations , open adressing and 
## How to Run

### Requirements

- Python 3.8+
- pandas

```bash
pip install pandas
```

### Run Experiments

**1. Compare Hash Functions**

```bash
python hash_function_comparison.py
```

**2. Compare Collision Resolution Methods**

```bash
python collision_strategy_test.py
```

---





