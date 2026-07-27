def print_table(number):
    """Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        # rjust(2) keeps the multiplier and result columns aligned
        result = number * i
        print(f"{number} x {str(i).rjust(2)} = {result}")


def print_tables_up_to_n(n):
    """Print multiplication tables for every number from 1 to n."""
    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("-" * 27)


if __name__ == "__main__":

    # -------------------------------------------------------------------
    # PART A — Single Table
    # -------------------------------------------------------------------
    print("=== PART A: Single Table ===")
    num = int(input("Enter a number: "))
    print_table(num)

    # -------------------------------------------------------------------
    # PART B — Bonus: Tables from 1 to N
    # -------------------------------------------------------------------
    print("\n=== PART B: Tables from 1 to N ===")
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)