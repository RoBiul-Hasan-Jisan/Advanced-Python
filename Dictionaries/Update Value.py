# Take a dictionary and increase all values by 5.
# Input: {'a': 10, 'b': 20}
# Output: {'a': 15, 'b': 25}


text = input("k:v separatre using , :")

text = {k : int(v)  for k , v in( item.split(":") for item in text.split(",")) }

text ={k : v + 5 for k , v in text.items()}




print(text)

