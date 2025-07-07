# DOC_TITLE: Fibonacci Sequence Example
# DOC_SUMMARY: Computes the first N Fibonacci numbers.
# DOC_NOTES: This sample demonstrates a basic loop and list usage.

### Define Fibonacci Function
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

### Print First 10 Fibonacci Numbers
print(fibonacci(10)) 