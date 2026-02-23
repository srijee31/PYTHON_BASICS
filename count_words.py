#Count Words in a Sentence

count_words= input("Enter a sentence to count words:     ")
words = count_words.split()
num_words = len(words)
print(f"Number of words in the sentence: {num_words}")  