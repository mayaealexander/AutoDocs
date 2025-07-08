# DOC_TITLE: Data Processing Example
# DOC_SUMMARY: Reads a list of numbers, filters and transforms them, and outputs results.
# DOC_NOTES: This sample demonstrates basic data processing steps: reading, filtering, transforming, and outputting.
# DOC_LINKS: https://docs.python.org/3/tutorial/datastructures.html

### Define Input Data
numbers = [1, 5, 8, 12, 15, 22, 29, 35, 42, 50]

### Filter Even Numbers
even_numbers = [n for n in numbers if n % 2 == 0]

### Square the Even Numbers
squared_evens = [n ** 2 for n in even_numbers]

### Print Results
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared evens:", squared_evens)