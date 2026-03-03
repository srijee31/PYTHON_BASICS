#Custom Length OTP Generator
import random

while True:
    try:
        length = int(input("Enter the desired length of the OTP: "))
        if length <= 0:
            print("Please enter a positive integer.\n")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.\n")

otp = ""
for _ in range(length):
    otp += str(random.randint(0, 9))

print(f"Your {length}-digit OTP is: {otp}")