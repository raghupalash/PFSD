# Mastering Python Functions

---

## I. Introduction to Functions

- Functions are reusable blocks of code that perform a specific task.
- They enhance code readability, reusability, and organization.

## II. Defining and Using Functions

- **Defining a Function:**
  - Syntax: `def function_name(arguments):`
  - Example: 
    ```python
    def greet(name):
        print("Hello, " + name)

	greet("Palash")
    ```

- **Returning from a Function:**
  - Using the `return` statement to send back a value.
  - Example:
    ```python
    def add(a, b):
        return a + b

	def returnTuple():
		return (1,2,3,4,5)
		# or return list, set, dict - any object really!
    ```

## III. Function Arguments

- **Positional Arguments:**
  - Defined by their position in the function call.
  - Example:
    ```python
    def power(base, exponent):
        return base ** exponent

	power(2, 3) # Cube of 2
    ```

- **Named Arguments:**
  - Specifying arguments by their parameter names.
  - Example:
    ```python
    def greet(name, message):
        print(message + ", " + name)

	greet(name="Palash", message="Hello!")
    ```

- **Default Arguments:**
  - Providing default values for parameters.
  - Example:
    ```python
    def greet(name, message="Hello"):
        print(message + ", " + name)
    ```

## IV. Writing the Main Function

- **Main Function in Python:**
  - Organizing code within a `if __name__ == "__main__":` block.
  - Example:
    ```python
    def main():
        # Your main code here

    if __name__ == "__main__":
        main()
    ```

## V. *args and **kwargs

- **Arbitrary Arguments:**
  - `*args` allows a function to accept any number of positional arguments.
  - Example:
    ```python
    def sum(*args):
        total = 0
        for num in args:
            total += num
        return total
    ```

- **Arbitrary Keyword Arguments:**
  - `**kwargs` allows a function to accept any number of keyword arguments.
  - Example:
    ```python
    def display_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

	display_info(name="Palash", message="Hello world", roll="23")
    ```

## VI. Lambda Functions

- Anonymous functions in Python.
- Defined using the `lambda` keyword.
- Can have any number of arguments but only one expression.
- Useful for short, simple functions.
- Syntax: `lambda arguments: expression`.

### Example:

- Regular function:
```python
def square(x):
    return x * x
```

- Equivalent lambda function:
```python
square_lambda = lambda x: x * x
```

- Usage with functions like `map()`, `filter()`, `sort()` for concise operations on iterables.

- Usage with `map`:
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

- Usage with `sort`:
```python
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
names.sort(key=lambda x: len(x))
print(names)  # Output: ['Bob', 'Eve', 'Alice', 'David', 'Charlie']

students = [(2, "Alice"), (1, "Bob"), (4, "Charlie"), (5, "Eve")]
students.sort(key=lambda x: x[0])
print(students) # Output: ["Bob", "Alice", "Charlie", "Eve"]
```

## VII. Function Decorators:

- Modify or extend the behavior of functions/methods without changing their code.
- Implemented as callable Python objects (functions).
- Take another function as input and return a new function.

### Example:

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

#Function decorated with uppercase_decorator:
@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

g = greet("Alice")
print(g) # Output: Hello, ALICE!
```




