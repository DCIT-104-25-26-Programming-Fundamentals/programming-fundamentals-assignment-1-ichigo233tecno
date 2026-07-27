def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, rounded to 2 decimals. Raises ValueError on b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """Return the remainder of a divided by b. Raises ValueError on b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b


def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b


def display_menu():
    """Print the menu options."""
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


def get_two_numbers():
    """Prompt for and return two numbers as floats."""
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second


if __name__ == "__main__":

    # Maps menu choice -> (function, symbol for display)
    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
        "5": (modulus, "%"),
        "6": (exponentiate, "**"),
    }

    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: Please enter a number between 1 and 7.")
            continue

        func, symbol = operations[choice]
        a, b = get_two_numbers()

        try:
            result = func(a, b)
            print(f"Result: {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")