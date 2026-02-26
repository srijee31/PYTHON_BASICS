#Count Digits in a Number (Without Converting to String)

number = int(input("Enter a number to count the digits: "))

if number == 0:
    count = 1
else:
    count = 0
    number = abs(number)   # Handle negative numbers

    while number > 0:
        number = number // 10
        count += 1

print(f"The number of digits is: {count}")