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

For more detailed output with test coverage:
```bash
pytest -v --cov=.
```

To run tests for a specific test file:
```bash
pytest tests/test_calculator.py -v
```

## Testing Framework Research

### Pytest vs Unittest: A Comparative Analysis

Python offers two prominent testing frameworks: **Pytest** and **Unittest**. Unittest is Python's built-in testing framework, part of the standard library, making it immediately available without additional installation. It follows a classical xUnit architecture where tests are organized into classes that inherit from `TestCase`. While Unittest is reliable and comprehensive, its verbose syntax and class-based structure can feel cumbersome for simple test cases. Pytest, on the other hand, is a third-party framework that emphasizes simplicity and readability. It uses simple function-based tests without requiring class inheritance, supports powerful fixtures for setup and teardown, and provides intuitive assertions using standard Python `assert` statements rather than specialized assertion methods.

The practical advantages of Pytest become apparent in real-world development. Pytest requires significantly less boilerplate code—a test function in Pytest is simply a function prefixed with `test_`, compared to Unittest's requirement to create a class inheriting from `TestCase`. Pytest's fixture system is more flexible and composable than Unittest's setup/teardown methods, allowing for sophisticated test parameterization and dependency injection. Additionally, Pytest provides superior debugging capabilities, clearer test output, and better integration with popular plugins for coverage analysis, mocking, and performance testing. The `-v` (verbose) flag and `-k` (filter) options make test execution more granular and informative.

**Justification for Choice:** Quick-Calc uses **Pytest** as its testing framework. This decision prioritizes developer experience and test maintainability. Pytest's cleaner syntax reduces cognitive load, allowing developers to focus on test logic rather than framework mechanics. Its powerful fixture system and plugin ecosystem provide the flexibility needed as the project scales. Furthermore, Pytest's superior error reporting and assertion introspection make debugging test failures faster and more intuitive, ultimately leading to higher code quality and faster development cycles.

---

**Last Updated:** March 2, 2026