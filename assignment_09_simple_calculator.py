# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    return a % b


def exponentiate(a, b):
    return a ** b


def get_numbers():
    while True:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            return first_number, second_number
        except ValueError:
            print("Error: Please enter valid numbers.")


def main():
    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        try:
            choice = int(input("Select an operation (1-7): "))
        except ValueError:
            print("Error: Invalid choice.")
            continue

        if choice == 7:
            print("Goodbye!")
            break

        if choice not in range(1, 7):
            print("Error: Invalid choice.")
            continue

        first_number, second_number = get_numbers()

        if choice == 1:
            result = add(first_number, second_number)
            operator = "+"
        elif choice == 2:
            result = subtract(first_number, second_number)
            operator = "-"
        elif choice == 3:
            result = multiply(first_number, second_number)
            operator = "*"
        elif choice == 4:
            result = divide(first_number, second_number)
            if result is None:
                print("Error: Cannot divide by zero.")
                continue
            operator = "/"
        elif choice == 5:
            result = modulus(first_number, second_number)
            operator = "%"
        else:
            result = exponentiate(first_number, second_number)
            operator = "**"

        print(f"Result: {first_number} {operator} {second_number} = {result}")


if __name__ == "__main__":
    main()

