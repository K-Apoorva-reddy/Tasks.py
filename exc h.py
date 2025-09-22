'''1.Syntax Error Check
Write a small code snippet that will produce a compile-time (syntax) error. Then fix it.
Example: Missing colon in an if statement.'''
if 5 > 3:
    print("5 is greater than 3")
#5 is greater than 3

'''2.ZeroDivisionError
Take two numbers from the user and perform division. Handle the case when the denominator is 0.'''
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Result is:", result)
finally:
    print("Division operation finished.")
#Enter numerator: 23
#Enter denominator: 21
#Result is: 1.0952380952380953
#Division operation finished. 

'''3.Ask the user for their age. Handle the case when the user enters a string instead of a number.'''
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Please enter a valid number for age!")
else:
    print("Your age is:", age)
finally:
    print("Program finished.")
#Enter your age: 21
#Your age is: 21
#Program finished.

'''4..TypeError
Try adding an integer and a string together. Handle the error.'''
try:
    num = 10
    text = "5"
    result = num + text   
except TypeError:
    print("Error: Cannot add an integer and a string!")
else:
    print("Result is:", result)
finally:
    print("Operation finished.")
#Error: Cannot add an integer and a string!
#Operation finished.


'''5.Finally Block
Write a program that takes an integer input. No matter what error occurs, print "Program Completed" using finally.'''
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid integer!")
finally:
    print("Program Completed")
#Enter an integer: 43
#You entered: 43  
#Program Completed

'''6.Multiple Exceptions
Ask the user for two numbers and perform division. Handle both ZeroDivisionError and ValueError separately.'''
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
else:
    print("Result is:", result)
finally:
    print("Division operation finished.")
#Enter numerator: 34
#Enter denominator: 28
#Result is: 1.2142857142857142
#Division operation finished.

'''7.File Handling Error
Try to open a file named student_data.txt. If it doesn’t exist, show a proper error message.'''
try:
    file = open("student_data.txt", "r")  # Try to open the file
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file 'student_data.txt' does not exist!")
finally:
    print("File operation completed.")
#Error: The file 'student_data.txt' does not exist!
#File operation completed

'''8.Catch All Exceptions
Write a program that asks for a number and prints its square. Use Exception to handle any unexpected errors.'''
try:
    num = float(input("Enter a number: "))
    square = num ** 2
except Exception as e:
    print("An error occurred:", e)
else:
    print("The square of the number is:", square)
finally:
    print("Program finished.")
#Enter a number: 12
#The square of the number is: 144.0
#Program finished.

'''9..Custom Error Message
If the user enters a negative age, raise a ValueError with a custom message: "Age cannot be negative!".'''
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")  # Custom error
except ValueError as e:
    print("Error:", e)
else:
    print("Your age is:", age)
finally:
    print("Program finished.")
#Enter your age: 21
#Your age is: 21
#Program finished.

'''10.Safe Calculator
Create a simple calculator (add, subtract, multiply, divide) that takes input from the user. Handle errors like 
invalid input, division by zero, etc.'''
try:
    print("Welcome to Safe Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operation!")  # Custom error for wrong operator

except ValueError as ve:
    print("Value Error:", ve)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Result:", result)
finally:
    print("Calculator program finished.")
#Welcome to Safe Calculator!
#Enter the first number: 9  
#Enter the second number: 4
#Choose operation (+, -, *, /): *
#Result: 36.0
#Calculator program finished.
exception handling