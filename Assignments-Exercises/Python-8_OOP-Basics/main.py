# ## Instructions

# 1. **Create the Car class**:

#    - Define a class called `Car`.
#    - Add a constructor method (`__init__`) to initialize the car’s `make`, `model`, and `year` attributes.

# 2. **Add the describe method**:

#    - Create a method called `describe` that returns a string with the description of the car (e.g., "This car is a 2020 Toyota Corolla.").

# 3. **Create an instance of the class**:

#    - In the main program, create an instance of the `Car` class with your chosen make, model, and year.
#    - Call the `describe` method on the object and print the result.

# 4. **Testing**:
#    - Test your code by creating different instances of the `Car` class with different values for `make`, `model`, and `year`.
#    - Print the description for each car instance.

# created a car class
class Car:
    # initiated init function
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # created describe function consisting of instance variables
    def describe(self):
        print(f"This car is a {self.year} {self.make} {self.model}.\n")

# marker for the creation of instances
print("Instantiations of Car classes: ")
my_car = Car("Tesla", "Model Y", 2025)
my_car.describe()

my_car2 = Car("BYD", "Han", 2025)
my_car2.describe()

my_car3 = Car("Honda", "Civic Type R", 2025)
my_car3.describe()

my_car4 = Car("Imperial", "Chrysler 300 Sport", 1962)
my_car4.describe()

# sample code
# # Define the Car class
# class Car:
#     # The constructor method to initialize the object
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     # Method to return a description of the car
#     def describe(self):
#         return f"This car is a {self.year} {self.make} {self.model}."

# # Create an instance of the Car class
# my_car = Car("Toyota", "Corolla", 2020)

# # Print the description of the car
# print(my_car.describe())
