# Library Management System

Current Version: **v2.0 - JSON Persistence**

## Overview

A console-based Library Management System built in Python using Object-Oriented Programming principles.

This project is being developed incrementally through multiple versions, with each version introducing new features and architectural improvements. The long-term goal is to evolve the application from a simple Python program into a full Django web application.

---

## Features

### Core Library Management
- Book registration
- Member registration
- Borrow books
- Return books
- Search books by title
- Track active loans
- Check book availability

### Data Persistence
- Save library data to JSON
- Load library data from JSON
- Automatic persistence after data modifications
- Object serialization and deserialization
- Restoration of relationships between books, members, and loans

---

## Project Structure

```text
library-management-system/
│
├── docs/
│
├── data/
│   └── library.json
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   └── loan.py
│
├── services/
│   ├── __init__.py
│   └── library.py
│
├── demo.py
├── main.py
└── README.md
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Git
- GitHub

---

## Version History

### v1.0 - Core OOP Implementation
- Book model
- Member model
- Loan model
- Library service
- Borrowing and returning books
- Search functionality
- Active loan tracking

### v2.0 - JSON Persistence
- Save library state to JSON
- Load library state from JSON
- Serialization (`to_dict`)
- Deserialization (`from_dict`)
- Date serialization/deserialization
- Automatic saving after updates

---

## Running the Demo

```bash
python3 demo.py
```

The demo showcases:

- Book registration
- Member registration
- Borrowing books
- Returning books
- Saving data
- Loading data

---

## Future Roadmap

### v3.0 - Automated Testing
- Unit testing with `unittest`
- Improved reliability
- Edge case coverage

### v4.0 - Command Line Interface (CLI)
- Interactive user menu
- User input handling
- Better user experience

### v5.0 - SQLite Database
- Replace JSON persistence with a relational database
- SQL queries
- Data integrity improvements

### v6.0 - Django Web Application
- Authentication
- Admin panel
- Web interface
- REST API
- Production deployment

---

## Author

**Shahzod Tursinboyev**

Python Backend Developer (in progress)