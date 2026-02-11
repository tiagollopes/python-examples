# New commands: class, __init__, self
# Classes are 'blueprints' for creating objects

class Car:
    # The __init__ method is the constructor
    # 'self' refers to the specific instance of the object
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_on = False

    def start_engine(self):
        self.is_on = True
        return f"The {self.model} engine is now running!"

    def get_info(self):
        return f"Car: {self.brand} {self.model} ({self.year})"

# --- Using the class (Creating Objects) ---

# Creating two different objects from the same class
my_car = Car("Toyota", "Corolla", 2024)
another_car = Car("Ford", "Mustang", 1969)

print(my_car.get_info())
print(my_car.start_engine())

print(another_car.get_info())
print(f"Is the engine on? {another_car.is_on}")
