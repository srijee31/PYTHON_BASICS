# prime number checker.

print("Welcome to Prime Number Checker!")
number = int(input("Enter the number to check if it is prime or not:    "))
if number <=1:
    print(f"{number} is not a prime number.")   
else:
    is_prime = True
    for i in range(2, int(number/2) + 1): # 2, 3
        if number % i == 0: 
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")