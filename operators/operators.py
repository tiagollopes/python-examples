# operators.py
# This example demonstrates the main operators in Python.
# It includes arithmetic, comparison, logical, assignment,
# identity, and membership operators.

print("=== Arithmetic Operators ===")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\n=== Comparison Operators ===")
x = 5
y = 10

print("Equal:", x == y)
print("Not equal:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater or equal:", x >= y)
print("Less or equal:", x <= y)

print("\n=== Logical Operators ===")
is_active = True
is_admin = False

print("AND:", is_active and is_admin)
print("OR:", is_active or is_admin)
print("NOT:", not is_active)

print("\n=== Assignment Operators ===")
n = 10
print("Initial value:", n)

n += 5
print("After += :", n)

n -= 3
print("After -= :", n)

n *= 2
print("After *= :", n)

n /= 4
print("After /= :", n)

print("\n=== Identity Operators ===")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

print("\n=== Membership Operators ===")
numbers = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)
