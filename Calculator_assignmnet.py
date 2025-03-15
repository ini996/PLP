#This python programme builds a calculator that accepts two numbers and
#operates on them using any of this operands, +,-, * and division.

import math
def calc():
    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        opeartion = input("Choose an opeartion (+, -, *, /): ")

        if opeartion == "+":
            result = num_1 + num_2
            print (f"{num_1} + {num_2} = {result}")
            
        elif opeartion == "-":
            result = num_1 - num_2
            print (f"{num_1} - {num_2} = {result}")
            
        elif opeartion == "*":
            result = num_1 * num_2
            print (f"{num_1} * {num_2} = {result}")

        elif opeartion == "/":
            if num2 == 0:
                print(f"indefinite: Division by zero is not allowed!")

            else:
                result = num_1 / num_2
                print (f"{num_1} / {num_2} = {result}")

        else:
            print ("Function definition. Choose from these operands (+, -, * or /)")
    except ValueError:
        print("Input not valid!, numbers only")

calc()
