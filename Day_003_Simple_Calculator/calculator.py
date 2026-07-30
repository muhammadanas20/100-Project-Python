first = float(input("Enter first number:").strip())
operation = input("Enter operator (-,+,/,*,%):").strip()
second = float(input("Enter second number:").strip())

if operation == "+":
    result = first + second 
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "%":
    result = first % second
else:
    print("Invalid operator!")
    
print(f"Result: {result}")