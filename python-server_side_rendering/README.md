# Python Server Side Rendering Project 🚀

A Flask project demonstrating various server-side rendering techniques and template management.

## Tasks Overview

### Task 0: Template Processing 📝
- File: `task_00_intro.py`
- Generates personalized invitation files from templates
- Handles placeholders for name, event title, date and location
- Includes error handling for various edge cases

### Task 1: Basic Flask Templates 🌐
- File: `task_01_jinja.py`
- Basic Flask application with Jinja templates
- Implements header and footer components
- Routes for Home, About, and Contact pages
- Demonstrates template inheritance and reusability

### Task 2: Dynamic Content ⚡
- File: `task_02_logic.py`
- Implements loops and conditionals in templates
- Reads items from JSON file
- Displays dynamic lists with error handling
- Demonstrates Jinja's control structures

### Task 3: Multiple Data Sources 📊
- File: `task_03_files.py`
- Handles multiple data sources (JSON, CSV)
- Implements product filtering
- Displays products in a formatted table
- Includes error handling for invalid inputs

### Task 4: Database Integration 💾
- File: `task_04_db.py`
- Adds SQLite database support
- Creates and manages product database
- Implements database queries and filtering
- Integrates with existing template system

## Project Setup 🛠️

1. Install Flask:
```bash
pip3 install Flask
```

2. Initialize database:
```bash
python3 products.db.py
```

## Running the Tasks ▶️


### Tasks 0-4:
```bash
python3 task_00_intro.py
python3 task_01_jinja.py
python3 task_02_logic.py
python3 task_03_files.py
python3 task_04_db.py
```

## Testing URLs 🔍

- Home: `http://localhost:5000/`
- About: `http://localhost:5000/about`
- Contact: `http://localhost:5000/contact`
- Items: `http://localhost:5000/items`
- Products (JSON): `http://localhost:5000/products?source=json`
- Products (CSV): `http://localhost:5000/products?source=csv`
- Products (SQL): `http://localhost:5000/products?source=sql`

## Directory Structure 📁
```
python-server_side_rendering/
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── create_db.py
├── products.json
├── products.csv
├── products.db
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    ├── product_display.html
    ├── header.html
    └── footer.html
```

## In Simple Terms 💡
This project is a web application that shows how to display information in different ways using Flask. It can read data from files (JSON and CSV) and a database (SQLite), then show this information on web pages. Think of it like a digital catalog that can get its product information from different sources and display it nicely on a website! 🎯