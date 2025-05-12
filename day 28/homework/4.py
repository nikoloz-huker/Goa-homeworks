user_input = input("Enter a sentence: ")
words = user_input.split()
words[0] = words[0].capitalize()
print(" ".join(words))