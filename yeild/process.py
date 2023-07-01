def generate_numbers(n):
    """Generator function to yield numbers from 0 to n-1."""
    for i in range(n):
        yield i

# Using the generator function
numbers = generate_numbers(5)

# Iterating over the generator
for num in numbers:
    print(num)
