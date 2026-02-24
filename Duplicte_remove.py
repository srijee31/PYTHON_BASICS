#Remove Duplicates From a List

numbers = input("Enter a list of numbers separated by spaces:     ")
num_list = [int(num) for num in numbers.split()]
unique_numbers = []
for num in num_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"List after removing duplicates: {unique_numbers}")

