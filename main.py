def count_words(text):
    words = text.split()
    return len(words)

text = input("Enter a sentence: ")
word_count = count_words(text)
print(f"Number of words: {word_count}")