# DOC_TITLE: Filtering and Transforming Lists with List Comprehensions
# DOC_SUMMARY: Demonstrates how to filter even numbers and compute their squares using Python list comprehensions.
# DOC_NOTE: List comprehensions provide a concise way to create lists by filtering and transforming elements.
# DOC_LINKS: [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

### Define the original list of numbers
# DOC_STEP_SUMMARY: This step initializes a list of integers to be used for filtering and transformation.
numbers = [1, 5, 8, 12, 15, 22, 29, 35, 42]  # Input list of integers

### Filter even numbers using a list comprehension
# DOC_STEP_SUMMARY: This step creates a new list containing only the even numbers from the original list.
even_numbers = [n for n in numbers if n % 2 == 0]  # Select numbers divisible by 2

### Compute the squares of the even numbers
# DOC_STEP_SUMMARY: This step generates a list of squares for each even number found in the previous step.
squared_evens = [n ** 2 for n in even_numbers]  # Square each even number

### Print the results
# DOC_STEP_SUMMARY: This step displays the original numbers, filtered even numbers, and their squares for verification.
print("Original numbers:", numbers)  # Show input list
print("Even numbers:", even_numbers)  # Show filtered even numbers
print("Squared evens:", squared_evens)  # Show squares of even numbers