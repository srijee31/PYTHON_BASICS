#sum of first n natural numbers of the given number

num= int(input("Enter a number to find the sum of first n natural numbers:     "))
sum = 0
for i in range(1, num + 1):
    sum = sum+i
print(f"The sum of the first {num} natural numbers is: {sum}")