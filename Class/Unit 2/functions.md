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

- **Lambda Functions:**
  - Anonymous functions defined using the `lambda` keyword.
  - Concise way to create small functions.
  - Example:
    ```python
    sqare = lambda x: x ** 2
    ```

## VII. Conclusion

- Functions are powerful tools in Python for code organization and reuse.
- Understanding function arguments and usage enhances code efficiency and readability.
- Continue exploring advanced topics like decorators and closures to further leverage the power of functions.
