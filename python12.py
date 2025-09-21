#simple caclualtor

print("###This is my calculator###")
print("Select the operation you want to perform"
      "\n1.Addition"
      "\n2.Subtraction"
      "\n3.Multiplication"
      "\n4.Division")
operation = input("Enter the operation you want to perform(1/2/3/4):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if operation == '1':
        print(f"{num1}+{num2}={abs(num1+num2)}")
elif operation == '2':
    print(f"{num1}-{num2}={num1-num2}")
elif operation == '3':
    print(f"{num1}*{num2}={num1*num2}")
elif operation == '4':
    if num2 != 0:
        print(f"{num1}/{num2}={num1/num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
