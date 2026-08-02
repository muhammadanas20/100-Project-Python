def calculate (left,operator,right):
    if(operator == "+"): return left + right
    if(operator == "-"): return left - right
    if(operator == "*"): return left * right
    if(operator == "/"): return left / right
    raise ValueError("Unknown operator")

try:
    left = float(input("First Number: "))
    operator = input("Operator: ").strip()
    right = float(input("Second Number: "))
    
    print(f"Result : {calculate(left,operator,right)}")
except ValueError as error:
    print(f"Input Problem: {error}")
except ZeroDivisionError:
    print("A number cannnot be divided by zero. ")   
    