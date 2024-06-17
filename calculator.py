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


# Display the menu
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


# Main program
while True:
    menu()

    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the choice is one of the options
    if choice in ['1', '2', '3', '4']:
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

    else:
        print("Invalid Input")

    # Ask if the user wants to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")

    if next_calculation.lower() != 'yes':
        break

print("Thank you for using the calculator!")