import math


# Define functions for the basic arithmetic operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def percentage(x, y):
    return (x / 100) * y


# Define functions for advanced operations
def exponent(x, y):
    return x ** y


def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number."
    else:
        return math.sqrt(x)


def log(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    else:
        return math.log(x, base)


# Display the menu
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Logarithm")


# Main program
while True:
    menu()

    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    # Check if the choice is one of the options
    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        if choice == '7':
            num1 = float(input("Enter the number: "))
            print(f"Square root of {num1} = {sqrt(num1)}")
        elif choice == '8':
            num1 = float(input("Enter the number: "))
            base = float(input("Enter the base (default is 10): ") or 10)
            print(f"Logarithm base {base} of {num1} = {log(num1, base)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice == '5':
                print(f"{num1}% of {num2} = {percentage(num1, num2)}")

            elif choice == '6':
                print(f"{num1} ^ {num2} = {exponent(num1, num2)}")

    else:
        print("Invalid Input")

    # Ask if the user wants to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")

    if next_calculation.lower() != 'yes':
        break

print("Thank you for using the calculator!")
