#Find the Second Largest Number in a List

numbers = input("Enter a list of numbers separated by spaces:     ")
num_list = [int(num) for num in numbers.split()]
if len(num_list) < 2:
    print("Please enter at least two numbers.")
else:
    largest = second_largest = float('-inf')
    for num in num_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        print("There is no second largest number (all numbers are the same).")
    else:
        print(f"The second largest number is: {second_largest}")