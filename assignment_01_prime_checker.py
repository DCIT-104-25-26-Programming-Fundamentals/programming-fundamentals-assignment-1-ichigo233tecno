def is_prime(n):
    """Return True if n is a prime number , False otherwise."""
    if n < 2:
        return False
    for divisor in range (2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")