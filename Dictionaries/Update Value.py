text = input("k:v separatre using , :")

text = {k : int(v)  for k , v in( item.split(":") for item in text.split(",")) }

text ={k : v + 5 for k , v in text.items()}




print(text)

