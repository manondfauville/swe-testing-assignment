# Quick-Calc

## Project Description

Quick-Calc is a Python-based calculator application designed to perform basic arithmetic operations with precision and ease. It provides a clean, intuitive interface for users to execute calculations while maintaining high code quality through comprehensive testing. Whether you're looking for a simple command-line calculator or integrating calculation functionality into your own project, Quick-Calc delivers reliable performance backed by a robust test suite.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manondfauville/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run Quick-Calc:
```bash
python main.py
```

Follow the on-screen prompts to enter numbers and select operations. The calculator supports addition, subtraction, multiplication, and division.

## How to Run Tests

Quick-Calc uses Pytest as its testing framework. To execute the test suite:

```bash
pytest
```


## Testing Framework Research

### Pytest vs Unittest: A Comparative Analysis

Python has two main testing frameworks: Pytest and Unittest. Unittest is built into Python and uses a class-based structure. You need to put tests inside classes that inherit from TestCase, and use special assertion methods. It works fine but can feel a bit long and heavy for small projects. Pytest is a third-party framework that lets you write tests as simple functions and just use normal Python assert statements. It also has fixtures to make setup and teardown easier, and it has a lot of useful plugins.

In practice, Pytest is easier to use. You don’t need to write a class for every test, and the output is easier to read when something fails. Fixtures are easier to work with than Unittest’s setup/teardown methods. It’s also easier to run only some tests or see verbose results. Overall, Pytest makes writing and maintaining tests faster and less frustrating, especially when the project grows.

Why Pytest for Quick-Calc: We chose Pytest because it’s simpler and faster to write tests with. It’s easy to read and understand, even for someone still learning, and it works well with the way we split the calculator into logic and GUI. The error messages are clear, and it will make adding new tests in the future much easier.
