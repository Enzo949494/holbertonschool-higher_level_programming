# Unit Testing in Python

## 🎯 Objective
Unit tests allow verifying the proper functioning of a function by testing different scenarios.

## 🛠 Main Components
1. unittest Module
Python standard library
Allows creating automated tests
Facilitates code verification
2. Test Class
````
python
class TestMyFunction(unittest.TestCase):
    def test_scenario1(self):
        # Specific test
        pass
````
3. Common Verification Methods
assertEqual(): Checks equality
assertIsNone(): Checks if value is None
assertTrue(): Checks if condition is true

## 📋 Common Test Types
* Empty list
* Single element list
* Normal list
* Negative values
* Mixed values
* Duplicate values

## 💡 Best Practices
* Test all possible cases
* Clearly name each test
* Verify different input types

## 🚀 Execution
````
bash
python3 -m unittest filename.py
````
