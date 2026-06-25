# 📘 Assignment: Modular Python Design

## 🎯 Objective

Learn how to organize a Python project into reusable modules, separate program logic from input/output, and make code easier to test and maintain.

## 📝 Tasks

### 🛠️ Create reusable modules

#### Description
Split program behavior into two modules: one for data processing and one for application flow.

#### Requirements
Completed program should:

- Define a module named `math_utils.py` with at least two functions: `add_numbers(a, b)` and `multiply_numbers(a, b)`.
- Define a module named `io_utils.py` with one function: `get_user_numbers()` that reads two numbers from the user and returns them as integers.
- Import and use these modules from `main.py`.

### 🛠️ Separate logic from input and output

#### Description
Keep the data-processing logic separate from the user interaction code so the functions can be reused and tested.

#### Requirements
Completed program should:

- Use `get_user_numbers()` from `io_utils.py` to read input.
- Use `add_numbers()` and `multiply_numbers()` from `math_utils.py` to compute results.
- Print both the sum and the product in `main.py` using a clear message.

### 🛠️ Add a reusable `main()` function

#### Description
Structure the program so it can be run directly or imported without immediately executing.

#### Requirements
Completed program should:

- Define a `main()` function in `main.py` that performs the program flow.
- Use `if __name__ == "__main__": main()` at the bottom of `main.py`.
- Ensure the program only asks for input when run directly.
