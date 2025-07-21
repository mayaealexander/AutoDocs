<!-- AUTO‑GENERATED doc for fibonacci.py -->
# Generate Fibonacci Sequence in Python

_Simple function to compute the first n Fibonacci numbers._


- This implementation uses a list to store the sequence and is efficient for small n.

## Step‑by‑step walk‑through
### 1. Step 1: Define the Fibonacci function
```python
def fibonacci(n):
    seq = [0, 1]  # Initialize list with first two Fibonacci numbers
    for i in range(2, n):  # Loop to generate remaining numbers up to n
        seq.append(seq[-1] + seq[-2])  # Append sum of last two numbers
    return seq[:n]  # Return first n numbers (handles n < 2)

```

### 2. Step 2: Print the first 10 Fibonacci numbers
```python
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```


## Resources
* [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)

<details><summary>Full source</summary>

```python

### Step 1: Define the Fibonacci function
def fibonacci(n):
    seq = [0, 1]  # Initialize list with first two Fibonacci numbers
    for i in range(2, n):  # Loop to generate remaining numbers up to n
        seq.append(seq[-1] + seq[-2])  # Append sum of last two numbers
    return seq[:n]  # Return first n numbers (handles n < 2)

### Step 2: Print the first 10 Fibonacci numbers
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>
Last updated: 2025-07-21
