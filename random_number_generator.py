import random

def generate_random_number(min_val, max_val):
    random_number = random.randint(min_val, max_val)
    return random_number

min_value = 1
max_value = 100
random_number = generate_random_number(min_value, max_value)
print(f"Random number between {min_value} and {max_value}: {random_number}")
