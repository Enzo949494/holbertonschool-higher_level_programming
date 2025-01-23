# Python Exceptions

* Python is a powerful and flexible programming language, especially with its exception handling. Here's an overview of key concepts:

### Difference Between Errors and Exceptions

* Errors are syntax problems that prevent code execution. Exceptions are events that occur during execution and disrupt the normal program flow.

### Using Exceptions

Exceptions allow managing errors and unexpected situations in code. They are used to:

* Capture and handle errors elegantly
* Allow the program to continue execution despite certain errors
* Provide useful information about encountered problems

### When to Use Exceptions

Use exceptions when:

* You have a code block that can sometimes fail based on unpredictable conditions
* You want to handle specific errors without interrupting the entire program
### Correct Exception Handling
```
python
try:
    # Code that might generate an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling a specific exception
    print("Error: Division by zero")
except Exception as e:
    # Handling other exceptions
    print(f"An error occurred: {e}")
else:
    # Code executed if no exception is raised
    print("Operation successful")
finally:
    # Code executed in all cases
    print("Processing complete")
```

### Raising an Exception

* Use the raise keyword to raise an exception:
```
python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = check_age(-5)
except ValueError as e:
    print(e)
```

### Cleanup Actions

* Use the finally block to execute cleanup code, whether an exception is raised or not:
```
python
try:
    file = open("example.txt", "r")
    # File processing
except FileNotFoundError:
    print("File not found")
finally:
    # Close file, even in case of error
    file.close()
```

### Common Exception Types
* ValueError: Incorrect value
* TypeError: Incorrect type
* ZeroDivisionError: Division by zero
* FileNotFoundError: File not found
* IndexError: Index out of bounds
* KeyError: Non-existent dictionary key

Python offers a powerful and flexible exception handling mechanism, enabling robust code writing and efficient error management.