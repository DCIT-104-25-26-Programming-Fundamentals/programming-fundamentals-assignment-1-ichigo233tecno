def calculate_sum(numbers):
    """Return the sum of all numbers in the list   """
    total = 0
    for num in numbers:
        total += num
        return total 

    def calculate_average(numbers):
        """Return the average of all numbers in the list."""
        total = calculate_sum(numbers)
        return total / len(numbers)

    def find_maximum(numbers):
        """Return the maximum number in the list """
        total = numbers[0]
        for num in numbers:
            if num > total:
                largest = num 
                return largest

            def find_minimum(numbers):
                """Return the minimum number in the list."""
                total = numbers[0]
                for num in numbers:
                    if num < total:
                        smallest = num
                        return smallest

                    if __name__ == "__main__":
                        numbers = [10, 20, 30, 40, 50]
                        print("Sum:", calculate_sum(numbers))
                        print("Average:", calculate_average(numbers))
                        print("Maximum:", find_maximum(numbers))
                        print("Minimum:", find_minimum(numbers))
                        
