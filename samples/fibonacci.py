# DOC_TITLE: Generate Fibonacci Sequence in Python
# DOC_SUMMARY: Simple function to produce the first N Fibonacci numbers as a list.
# DOC_NOTE: This implementation uses a list to store the sequence and iteratively builds it up.
# DOC_LINKS: [Fibonacci Number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
# DOC_LINKS: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Define Fibonacci sequence generator function
# DOC_STEP_SUMMARY: This step defines a function that returns a list containing the first n Fibonacci numbers using an iterative approach.
def fibonacci(n):
    seq = [0, 1]  # Start sequence with first two Fibonacci numbers
    for i in range(2, n):  # Generate remaining numbers up to n
        seq.append(seq[-1] + seq[-2])  # Add sum of last two numbers to sequence
    return seq[:n]  # Return sequence truncated to n elements

### Call function and print result
# DOC_STEP_SUMMARY: This step calls the Fibonacci function with n=10 and prints the resulting list of numbers.
print(fibonacci(10))  # Output first 10 Fibonacci numbers