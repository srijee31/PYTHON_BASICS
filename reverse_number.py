#Reverse a number WITHOUT converting to string.

number = int(input("Enter a number to reverse:     "))
reversed_number = 0
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = (reversed_number * 10) + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the original number
print(f"The reversed number is: {reversed_number}")