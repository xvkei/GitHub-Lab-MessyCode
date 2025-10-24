# This program adds two numbers and prints the result

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def main():
    print("This is a simple adder program")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    result = add_numbers(a, b)
    print("The sum is:", result)

if __name__ == "__main__":
    main()
# KELVIN CODE
