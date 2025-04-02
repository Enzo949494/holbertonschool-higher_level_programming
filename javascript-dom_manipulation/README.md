# 🚀 JavaScript DOM Manipulation

## 📝 Overview
This project focuses on mastering DOM manipulation in JavaScript. Through a series of practical exercises, we explore how to interact with HTML elements, handle events, modify content and styling, and fetch data from APIs - all without reloading the page.

## 🎯 Learning Objectives
- Understanding how to select HTML elements using JavaScript
- Manipulating HTML element content, attributes, and styles
- Working with event listeners to respond to user interactions
- Creating and adding new elements to the DOM
- Modifying CSS classes dynamically
- Using the Fetch API to retrieve data from external sources
- Working with Promises in JavaScript

## 📂 Project Structure
The project consists of the following files:

### 0-script.js
- **Task**: Change the text color of the header element to red (#FF0000)
- **Methods used**: `document.querySelector()`

### 1-script.js
- **Task**: Update header text color to red when user clicks on element with id "red_header"
- **Methods used**: `getElementById()`, `querySelector()`, event listeners

### 2-script.js
- **Task**: Add the "red" class to the header when user clicks on element with id "red_header"
- **Methods used**: `classList.add()`

### 3-script.js
- **Task**: Toggle between "red" and "green" classes on the header when user clicks on element with id "toggle_header"
- **Methods used**: `classList.contains()`, `classList.add()`, `classList.remove()`

### 4-script.js
- **Task**: Add a new `<li>` element to a list when user clicks on element with id "add_item"
- **Methods used**: `createElement()`, `appendChild()`, `textContent`

### 5-script.js
- **Task**: Update the header text to "New Header!!!" when user clicks on element with id "update_header"
- **Methods used**: Event handling, `textContent`

### 6-script.js
- **Task**: Fetch a Star Wars character name from an API and display it
- **Methods used**: Fetch API, Promises, DOM manipulation

### 7-script.js
- **Task**: Fetch Star Wars movie titles from an API and display them in a list
- **Methods used**: Fetch API, Array manipulation, DOM creation

### 8-script.js
- **Task**: Fetch a greeting in French from an API and display it
- **Methods used**: Fetch API, DOMContentLoaded event, Promise handling

## ⚙️ Requirements
- All files interpreted on Chrome browser (version 57.0 or later)
- Code is semistandard compliant
- No usage of `var` keyword
- No page reloads for DOM manipulations or data fetching

## 🔍 Usage
Each JavaScript file is designed to work with its corresponding HTML file. To test:
1. Open the HTML file in Chrome browser
2. Interact with the specified element
3. Observe the DOM changes as defined in each task

## 🏁 Conclusion
This project demonstrates the power of JavaScript for creating dynamic web pages through DOM manipulation. By using modern JavaScript techniques including event handling, DOM traversal and modification, and asynchronous API calls, we can create interactive web experiences without requiring page reloads. These skills form the foundation of modern front-end web development.