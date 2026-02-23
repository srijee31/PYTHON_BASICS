# count ovels in a string

input_string = input("Enter a string to count vowels:     ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count = vowel_count + 1
print(f"Number of vowels in the string: {vowel_count}")     