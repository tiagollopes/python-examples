# New commands: def, return
# This file contains 10 examples of functions for beginners

# 1. Basic greeting
def welcome():
    return "Welcome to Python Functions!"

# 2. Greeting with parameter
def greet_user(name):
    return f"Hello, {name}!"

# 3. Simple sum
def add_numbers(a, b):
    return a + b

# 4. Check if a number is even
def is_even(number):
    return number % 2 == 0

# 5. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 6. Calculate average of a list
def get_average(numbers):
    return sum(numbers) / len(numbers)

# 7. Find the largest number in a list
def find_max(numbers_list):
    return max(numbers_list)

# 8. Repeat a string
def repeat_text(text, times):
    return text * times

# 9. Simple discount calculator
def apply_discount(price, percentage):
    return price - (price * (percentage / 100))

# 10. Count characters in a word
def count_letters(word):
    return len(word)

# --- TESTING THE FUNCTIONS ---
print(welcome())
print(greet_user("Tiago"))
print(f"Sum 10+5: {add_numbers(10, 5)}")
print(f"Is 7 even? {is_even(7)}")
print(f"25°C in Fahrenheit: {celsius_to_fahrenheit(25)}")
print(f"Average: {get_average([10, 20, 30])}")
print(f"Max value: {find_max([5, 82, 12])}")
print(f"Repeat: {repeat_text('Python! ', 3)}")
print(f"Price with 10% discount: {apply_discount(100, 10)}")
print(f"Letters in 'Python': {count_letters('Python')}")
