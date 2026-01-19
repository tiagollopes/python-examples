# operators.py
# This example demonstrates the main operators in Python.
# It includes arithmetic, comparison, logical, assignment,
# identity, membership, and float operations.

print("=== Arithmetic Operators (int) ===")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\n=== Arithmetic Operators (float) ===")
price = 19.90
quantity = 2.5

total = price * quantity
average = total / quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
print("Average:", average)

print("\n=== Comparison Operators ===")
x = 5.5
y = 10.0

print("Equal:", x == y)
print("Not equal:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater or equal:", x >= y)
print("Less or equal:", x <= y)

print("\n=== Logical Operators ===")
is_active = True
has_discount = False

print("AND:", is_active and has_discount)
print("OR:", is_active or has_discount)
print("NOT:", not is_active)

print("\n=== Assignment Operators ===")
n = 10.0
print("Initial value:", n)

n += 5.5
print("After += :", n)

n -= 2.5
print("After -= :", n)

n *= 2
print("After *= :", n)

n /= 3
print("After /= :", n)

print("\n=== Identity Operators ===")
a = [1.0, 2.0, 3.0]
b = a
c = [1.0, 2.0, 3.0]

print("a is b:", a is b)
print("a is c:", a is c)

print("\n=== Membership Operators ===")
values = [1.5, 2.5, 3.5]

print("2.5 in values:", 2.5 in values)
print("5.0 not in values:", 5.0 not in values)
