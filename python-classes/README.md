
# Python Classes - Square Project

## Description

This project implements a Square class in Python that allows defining a square with size and position attributes. The class includes methods to calculate the square's area and display it on the screen.

## Features

### Attributes:

* size: Square size (must be a positive integer)
* position: Square position (must be a tuple of two positive integers)
### Methods:
* area(): Calculates and returns the square's area
* my_print(): Displays the square on screen using # character, respecting its position
## Requirements
* Python 3.x
* No additional libraries required
### Installation
````
bash
# Clone the repository
git clone https://github.com/yourusername/square-project.git
# Navigate to project directory
cd square-project
Usage
Creating an Instance
python
from square import Square

# Create a square with size 3 at position (0, 0)
my_square = Square(3)

# Create a square with size 3 at position (1, 1)
my_square_with_position = Square(3, (1, 1))
````

### Calculating Area
````
python
area = my_square.area()
print("Area:", area)  # Outputs: Area: 9
````
### Printing the Square
````
python
my_square.my_print()
Full Example
python
from square import Square

# Create a square of size 3 at position (1, 1)
my_square = Square(3, (1, 1))
my_square.my_print()

print("--")

# Change size to 5 and display
my_square.size = 5
my_square.my_print()

print("--")

# Change position to (2, 2) and display
my_square.position = (2, 2)
my_square.my_print()
````
## Error Handling
### Size Validation
* Attempting to assign a non-integer value to size raises a TypeError
* Attempting to assign a negative value to size raises a ValueError
### Position Validation
* Attempting to assign an invalid position raises a TypeError
### Advanced Features
* Private attribute management
* Getter and setter methods
* Input validation
* Flexible object creation
### Best Practices Demonstrated
* Encapsulation
* Data validation
* Object-oriented programming principles
### Potential Improvements
* Add rotation method
* Implement color attribute
* Create comparison methods between squares
