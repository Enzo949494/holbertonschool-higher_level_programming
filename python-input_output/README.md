# ✨ Python I/O Basics - Project 📝
## Description
This project shows the simplest ways to do Input/Output (I/O) in Python.
## Features
* ⌨️ User Input: Get text from the user.
* 📺 Screen Output: Display text and values.
* 📖 File Reading: Read text from files.
* ✍️ File Writing: Write text to files.
## Requirements
* Python 3.x
* No extra libraries needed.
## Usage
### 1. Get Input:
````
python
name = input("Enter name: ")
print("Hello,", name)
````
### 2. Display Output:
````
python
print("Text:", 123)
````
### 3. Read File:
````
python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
````
### 4. Write File:
````
python
with open("file.txt", "w") as f:
    f.write("New text\n")
````
### Error Handling:
* Handle errors, like missing files:
````
python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
````
That's it! These are the key things for I/O in Python.
