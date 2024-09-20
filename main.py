import random

def generate_random_numbers():
    # Choose a random number of elements between 5 and 15
    num_elements = random.randint(5, 15)
    
    # Generate the random numbers
    random_numbers = [random.randint(0, 100) for _ in range(num_elements)]
    
    return random_numbers

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
random_numbers = generate_random_numbers()
average = calculate_average(random_numbers)

print("Random Numbers:", random_numbers)
print("Average:", average)