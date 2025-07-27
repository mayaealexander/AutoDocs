<!-- AUTO‑GENERATED doc for data_processing.py -->
# Filtering and Transforming Lists with List Comprehensions

_Demonstrates how to filter even numbers and compute their squares using Python list comprehensions._




**Notes:**
> List comprehensions provide a concise way to create lists by filtering and transforming elements.


## Step‑by‑step walk‑through
### Step 1: Define the original list of numbers
This step initializes a list of integers to be used for filtering and transformation.

```python
numbers = [1, 5, 8, 12, 15, 22, 29, 35, 42]

```

### Step 2: Filter even numbers using a list comprehension
This step creates a new list containing only the even numbers from the original list.

```python
even_numbers = [n for n in numbers if n % 2 == 0]

```

### Step 3: Compute the squares of the even numbers
This step generates a list of squares for each even number found in the previous step.

```python
squared_evens = [n ** 2 for n in even_numbers]

```

### Step 4: Print the results
This step displays the original numbers, filtered even numbers, and their squares for verification.

```python
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared evens:", squared_evens)
```


## Resources
* [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

<details><summary>Full source</summary>

```python

### Define the original list of numbers
numbers = [1, 5, 8, 12, 15, 22, 29, 35, 42]  # Input list of integers

### Filter even numbers using a list comprehension
even_numbers = [n for n in numbers if n % 2 == 0]  # Select numbers divisible by 2

### Compute the squares of the even numbers
squared_evens = [n ** 2 for n in even_numbers]  # Square each even number

### Print the results
print("Original numbers:", numbers)  # Show input list
print("Even numbers:", even_numbers)  # Show filtered even numbers
print("Squared evens:", squared_evens)  # Show squares of even numbers
```
</details>
Last updated: 2025-07-27
