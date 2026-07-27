def generate_fibonacci(n):
    """Return a list of the first n Fibonacci numbers, using a loop."""
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci(num):
    """Return True if num appears in the Fibonacci sequence, using a loop."""
    if num < 0:
        return False

    a, b = 0, 1

    # Walk the sequence up until we reach or pass num
    while a < num:
        a, b = b, a + b

    return a == num


if __name__ == "__main__":

    # -------------------------------------------------------------------
    # PART A — Print the First N Terms
    # -------------------------------------------------------------------
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        sequence = generate_fibonacci(n)
        sequence_str = " ".join(str(num) for num in sequence)
        print(f"Fibonacci sequence: {sequence_str}")

    # -------------------------------------------------------------------
    # PART B — Check if a Number Belongs to the Sequence
    # -------------------------------------------------------------------
    num = int(input("\nEnter a number to check: "))

    if is_fibonacci(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")