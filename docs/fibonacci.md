<!-- AUTO-GENERATED doc for samples/fibonacci.py -->
# Generate Fibonacci Sequence in Python





## Step-by-step walk-through
### 1. Define the Fibonacci function
```python
def fibonacci(n):
    seq = [0, 1]  # Initialize sequence with first two Fibonacci numbers
    for i in range(2, n):  # Loop from 2 up to n-1
        seq.append(seq[-1] + seq[-2])  # Add next Fibonacci number to the list
    return seq[:n]  # Return only the first n elements
```

### 2. Print the first 10 Fibonacci numbers
```python
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```


* [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
<details><summary>Full source</summary>

```python
# DOC_TITLE: Generate Fibonacci Sequence in Python
# DOC_BLURB: Simple function to generate the first N Fibonacci numbers.
# DOC_NOTE: The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# DOC_LINKS: [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)

### Define the Fibonacci function
def fibonacci(n):
    seq = [0, 1]  # Initialize sequence with first two Fibonacci numbers
    for i in range(2, n):  # Loop from 2 up to n-1
        seq.append(seq[-1] + seq[-2])  # Add next Fibonacci number to the list
    return seq[:n]  # Return only the first n elements

### Print the first 10 Fibonacci numbers
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

</details>
Last updated: 2025-07-20

