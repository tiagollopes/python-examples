# Basic example of Exception Handling for beginners
# This script demonstrates how to catch errors gracefully

try:
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter a valid integer number.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

finally:
    print("Operation finished. This block always runs.")
