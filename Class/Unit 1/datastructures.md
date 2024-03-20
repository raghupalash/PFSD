# Exploring Data Structures and Operations in Python: Strings, Lists, Sets, Tuples, and Dictionaries

---

## Strings

Strings are sequences of characters, enclosed within single, double, or triple quotes. Let's start by exploring common operations and built-in functions for strings:

- **Concatenation:** Combining strings using the `+` operator.
- **Indexing and Slicing:** Accessing individual characters or substrings using index notation and slicing.
- **Length:** Finding the length of a string using the `len()` function.
- **Conversion:** Converting between uppercase and lowercase using `upper()` and `lower()` methods. Using `isalpha()`, `isnumeric()` and `isalnum()` methods.
- **Splitting and Joining:** Splitting a string into a list of substrings using `split()` and joining a list of strings into a single string using `join()`.

## Lists

Lists are ordered collections of items, separated by commas and enclosed within square brackets. Let's explore their operations:

- **Indexing and Slicing:** Similar to strings, accessing elements and sublists using index notation and slicing.
- **Appending and Extending:** Adding elements to the end of a list using `append()` and extending a list with another list using `extend()`.
- Items of different types allowed. But how does that work? - Everything's an object!
- **Inserting and Deleting:** Inserting elements at a specific position with `insert()` and removing elements by value with `remove()`.
- **Sorting and Reversing:** Sorting a list using `sort()` and reversing the order of elements with `reverse()`.
- `for`, `in`, `index`
- List comprehension. 
	- `new_list = [item for item in old_list if condition]`
- Packing and unpacking
- Homework - 
	- Write code to use list methods like `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse` etc.
	- Write code to use built in methods on list like: `len`, `max`, `min`, `sorted`, `map`, `enumerate`, `zip` etc.
	- Write code to slice a list - reverse the list using slicing.

## Sets

Sets are unordered collections of unique elements, enclosed within curly braces. Key operations include:

- **Adding and Removing:** Adding elements to a set using `add()` and removing elements with `remove()` or `discard()`.
- **Union, Intersection, and Difference:** Combining sets with `union()`, finding common elements with `intersection()`, and finding differences with `difference()` and `symmetric_difference()`.
- **Subset and Superset:** Checking if a set is a subset or superset of another set using `issubset()` and `issuperset()`.
- Homework: Learn about `FrozenSet`.

## Tuples

Tuples are immutable ordered collections, enclosed within parentheses. Though they cannot be modified after creation, they still offer useful operations:

- **Indexing and Slicing:** Accessing elements and sub-tuples using index notation and slicing.
- **Packing and Unpacking:** Assigning multiple variables at once by packing and unpacking tuples.
- **Functions and Methods:** Utilizing built-in functions like `len()` and methods like `count()` and `index()`.

## Dictionaries

Dictionaries are unordered collections of key-value pairs, enclosed within curly braces and separated by colons. Key operations include:

- **Accessing Values:** Accessing values by keys using square bracket notation.
- **Adding and Updating:** Adding new key-value pairs or updating existing ones using square brackets.
- **Removing:** Removing key-value pairs using `del` statement or `pop()` method.
- **Iterating:** Iterating over keys, values, or key-value pairs using `keys()`, `values()`, and `items()` methods.

Happy Coding!