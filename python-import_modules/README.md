# Python - import & modules

## Key Learning Objectives

1. Importing Functions
Import specific functions from other files
Use precise import statements
Avoid using * or __import__() for imports

2. Module Creation and Usage
Create modules by saving Python code in .py files
Import and use functions from custom modules
Prevent code execution during import using if __name__ == "__main__":

3. Command Line Arguments
Use sys.argv to handle command-line arguments
Process multiple arguments dynamically
Perform operations like argument counting and addition

## Sample Import Techniques

### Basic Function Import
```
from module import function_name

#Example
from add_0 import add
a = 1
b = 2
print(f"{a} + {b} = {add(a, b)}")
```

## Preventing Import Execution
```
if __name__ == "__main__":
    # Code here runs only when script is directly executed
````

### Project Requirements

* Use Python 3.10.* on Ubuntu 22.04 LTS
* Follow pycodestyle (version 2.7.*)
* Make files executable
* Start scripts with #!/usr/bin/python3
* End files with a new line

### Advanced Techniques Demonstrated

* Dynamic argument handling
* Modular code organization
* Flexible function imports
* Preventing unintended code execution
