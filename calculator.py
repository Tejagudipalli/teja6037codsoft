# Define functions for each operation
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    print("Error: Cannot divide by zero.")
    return None
  else:
    return num1 / num2

# Main program loop
while True:
  try:
    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for operation
    operator = input("Choose operation (+, -, *, /): ")

    # Perform calculation based on operator
    if operator == "+":
      result = add(num1, num2)
    elif operator == "-":
      result = subtract(num1, num2)
    elif operator == "*":
      result = multiply(num1, num2)
    elif operator == "/":
      result = divide(num1, num2)
    else:
      print("Invalid operator. Please use +, -, *, or /.")
      result = None  # Indicate error

    # Display result if no errors
    if result is not None:
      print(f"{num1} {operator} {num2} = {result}")

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
      break

  except ValueError:
    print("Invalid input. Please enter numbers only.")

print("Calculator ending. Thank you!")





















145