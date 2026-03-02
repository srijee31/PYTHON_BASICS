#Program: Character Frequency Counter

text= input("Enter a string to count character frequency:     ").lower() # Convert to lowercase for case-insensitive counting
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1 
print("Character Frequency:")
for char, count in frequency.items():
    print(f"{char}: {count}")
    