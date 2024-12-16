# simple-math.py
def calculate_square(numbers):
    """
    This function takes a list of numbers and returns their squares.
    """
    result = [num ** 2 for num in numbers]
    return result

def main():
    print("Welcome to the square calculator!")
    numbers = [1, 2, 3, 4, 5]
    squares = calculate_square(numbers)
    print(f"Original numbers: {numbers}")
    print(f"Squares: {squares}")

if __name__ == "__main__":
    main()
