# DOC_TITLE: Generate Fibonacci Sequence in Python
# DOC_SUMMARY: Simple function to compute the first n Fibonacci numbers.
# DOC_NOTE: This implementation uses a list to store the sequence and iteratively builds it up.
# DOC_LINKS: [Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
# DOC_LINKS: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Define the Fibonacci sequence generator
# DOC_STEP_SUMMARY: This step defines a function that returns the first n numbers of the Fibonacci sequence as a list.
def fibonacci(n):
    seq = [0, 1]  # Start sequence with first two Fibonacci numbers
    for i in range(2, n):  # Generate remaining numbers up to n
        seq.append(seq[-1] + seq[-2])  # Add sum of last two numbers to sequence
    return seq[:n]  # Return sequence truncated to n elements

### Print the first 10 Fibonacci numbers
# DOC_STEP_SUMMARY: This step demonstrates the function by printing the first 10 Fibonacci numbers.
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]