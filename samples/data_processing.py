numbers = [1, 5, 8, 12, 15, 22, 29, 35, 42]
even_numbers = [n for n in numbers if n % 2 == 0]
squared_evens = [n ** 2 for n in even_numbers]

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared evens:", squared_evens)