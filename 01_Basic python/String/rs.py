sentence = input("Enter a sentence: ")

# Split the sentence into words, reverse the list, and join back
reversed_sentence = " ".join(sentence.split()[::-1])

print("Reversed sentence:", reversed_sentence)