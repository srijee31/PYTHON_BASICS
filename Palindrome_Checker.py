#Palindrome Checker (Without Slicing)

input_string = input("Enter a string to check if it's a palindrome:     ")
# Remove spaces and convert to lowercase for accurate comparison
processed_string = input_string.replace(" ", "").lower()
is_palindrome = True
for i in range(len(processed_string) // 2):
    if processed_string[i] != processed_string[-(i + 1)]:
        is_palindrome = False
        break   
if is_palindrome:
    print(f"{input_string} is a palindrome.")
else:    print(f"{input_string} is not a palindrome.")