<!-- AUTO‑GENERATED doc for fibonacci.py -->
# Generate Fibonacci Sequence in Python

_Simple function to compute the first n Fibonacci numbers._


- This implementation uses a list to store the sequence and iteratively builds it up.

## Step‑by‑step walk‑through
### Step 1: Define the Fibonacci sequence generator
This step defines a function that returns the first n numbers of the Fibonacci sequence as a list.

```python
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

```

### Step 2: Print the first 10 Fibonacci numbers
This step demonstrates the function by printing the first 10 Fibonacci numbers.

```python
print(fibonacci(10))
```


## Resources
* [Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
* [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<details><summary>Full source</summary>

```python

### Define the Fibonacci sequence generator
def fibonacci(n):
    seq = [0, 1]  # Start sequence with first two Fibonacci numbers
    for i in range(2, n):  # Generate remaining numbers up to n
        seq.append(seq[-1] + seq[-2])  # Add sum of last two numbers to sequence
    return seq[:n]  # Return sequence truncated to n elements

### Print the first 10 Fibonacci numbers
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>
Last updated: 2025-07-27
