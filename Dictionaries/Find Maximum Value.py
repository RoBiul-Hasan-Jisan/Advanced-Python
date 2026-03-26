# Find the key with the highest value.


# Input: {'a': 10, 'b': 50, 'c': 30}
# Output: b

text = input("k:v separatre using , :")

text = {k : int(v) for k,v in (it.split(":") for it in text.split(","))}


mina = max(text,key = text.get)

print(f"{mina} : {text[mina]}")