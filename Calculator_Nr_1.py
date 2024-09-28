from colorama import Fore

# This function adds two numbers 
def add(x, y):
    return x + y 

# This function subtracts two numbers
def subtract(x, y):
    return x - y 

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print(Fore.LIGHTCYAN_EX + "Select an option.")
print("(1) Add")
print("(2) Subtract")
print("(3) Multiply")
print("(4) Divide")

while True:
    
    # Take input from user
    choice = input(Fore.LIGHTCYAN_EX +  "Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Please enter a valid number")
            continue  # Restart the loop after invalid input
        
        if choice == '1':
            print(Fore.LIGHTGREEN_EX + f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(Fore.LIGHTGREEN_EX  + f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(Fore.LIGHTGREEN_EX  + f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(Fore.LIGHTGREEN_EX  + f"{num1} / {num2} = {divide(num1, num2)}")

        # Check if the user wants another calculation
        next_calculation = input(Fore.LIGHTCYAN_EX + "Let's do another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break

    else:
        print(Fore.LIGHTRED_EX + "Invalid Input")
