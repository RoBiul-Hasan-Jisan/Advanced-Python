'''
Write a Python function that counts how many times each word appears in a given string, and returns the result as a dictionary.
'''

def count_word(text):
    words = text.lower().split()
    wc = {}

    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]= 1

    return wc

text = "Hello hello world"
result = count_word(text)
print(result)
