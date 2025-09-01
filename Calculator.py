# Simple Calculator Program
# This is a basic calculator for addition, subtraction, multiplication, division
# Added error handling for bad inputs and division by zero

# Adding two numbers
def add(x, y):
    return x + y

# Multiply function, returns product of two numbers
def multiply(x, y):
    return x * y

# Subtracts second number from first
def subtract(x, y):
    return x - y

# Divides first by second, checks for zero
def divide(x, y):
    if y == 0:
        return "Error: Can't divide by zero!"
    return x / y

# Main calculator function
def calculator():
    print("Welcome to Simple Calculator!")  # Welcome message
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        # Get operation choice
        choice = int(input("Enter choice (1-4): "))
        
        # Check if choice is valid
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Pick 1, 2, 3, or 4.")
            return
        
        # user base choose number
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Just print result
        print(f"You entered: {num1} and {num2}") 
        
        # you want to chose 
        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
            
    except ValueError:
        print("Error: Enter valid numbers please!")  # minnor error 

# starting here 
if __name__ == "__main__":
    calculator()
    print("Thanks for using the calculator!") 