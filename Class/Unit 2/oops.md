# Object-Oriented Programming (OOP) in Python

## Introduction to OOP:

- OOP revolves around objects, which combine data (attributes) and behaviors (methods).
- Python supports OOP principles effectively.

## Object:

- An instance of a class encapsulating data and behaviors.
- It combines data (attributes) and behaviors (methods) into a single entity.
- Everything in python is an object, be it `int`, `bool`, `string`, `list`, `set` and even functions!

## Class:

- Blueprint for creating objects.
- Defines structure and behavior.
- Created using the `class` keyword.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

# Creating objects of class
car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model S")
```

## `self` Keyword:

- Refers to the instance of the class itself.
- Used to access variables and methods within the class.
- Must be the first parameter in any method definition within a class.

## Class Methods and Object Methods:

- Class methods are bound to the class itself and can access class variables.
- Object methods are bound to the object instance and can access instance variables.
- Class methods are defined using the `@classmethod` decorator.
- Object methods are defined without any decorator.

```python
class MyClass:
    class_variable = "Class Variable"
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    def object_method(self):
        return self.class_variable
```

## Encapsulation:

- Bundles data and methods into a single unit (class).
- Controls access to data using access modifiers.
    - For `protected` use single underscore, for eg. `_salary`.
    - For `private` use doube underscore, for eg. `__salary`.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

# Creating an Employee object
employee = Employee("John", 50000)
print(employee.name)  # Accessing public attribute
print(employee.get_salary())  # Accessing private attribute using method
```


## Abstraction:

- Hides complex implementation details.
- Focuses on essential features.
- Achieved through classes and methods.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

## Polymorphism:

- Functions/methods behave differently based on the object.
- Allows treating objects of different classes as objects of a common superclass.
- Achieved through method overriding.
- Method overloading not supported in python

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic behavior
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

## Inheritance:

- Mechanism for a subclass to inherit attributes and methods from a superclass.
- Promotes code reusability.
- Creates a hierarchy of classes.

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return super().speak() + ", but I bark!"

# Inheriting and overriding method
dog = Dog()
print(dog.speak())
```

## Using the `super()` Method:

- Calls methods of the superclass from the subclass.
- Useful for invoking superclass methods when overriding in the subclass.
- Ensures proper inheritance and method chaining.

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return super().speak() + ", but I bark!"

# Using super() to call superclass method
dog = Dog()
print(dog.speak())
```