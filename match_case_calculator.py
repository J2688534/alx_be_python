# Ask for two numbers and conver them to floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = inputoperation = input("Choose the operation (+, -, *, /): ")
 

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero."
    case _:
        result = "Invalid operation selected."

        print(f"The result is: {result}")


