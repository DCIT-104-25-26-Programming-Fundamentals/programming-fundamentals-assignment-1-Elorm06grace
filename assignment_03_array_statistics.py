# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    current_max = numbers[0]
    for value in numbers[1:]:
        if value > current_max:
            current_max = value
    return current_max


def calculate_minimum(numbers):
    current_min = numbers[0]
    for value in numbers[1:]:
        if value < current_min:
            current_min = value
    return current_min


def read_numbers():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return None

    if count <= 0:
        print("Error: N must be a positive integer.")
        return None

    values = []
    for i in range(1, count + 1):
        while True:
            try:
                value = float(input(f"Enter number {i}: "))
                break
            except ValueError:
                print("Error: Please enter a valid number.")
        values.append(value)

    return values


def main():
    numbers = read_numbers()
    if numbers is None:
        return

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {calculate_maximum(numbers)}")
    print(f"Minimum: {calculate_minimum(numbers)}")


if __name__ == "__main__":
    main()

