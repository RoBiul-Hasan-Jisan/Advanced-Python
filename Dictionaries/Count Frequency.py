text1 = input("Enter text :").lower().replace(" ","")
 #  Hello hello world
 # {'h': 2, 'e': 2, 'l': 5, 'o': 3, 'w': 1, 'r': 1, 'd': 1}
 
text = input("Enter text: ").lower().split() 
 #  Hello hello world
 # output Hello : 2  world : 1
 # 2 2 4 5 6 7 4 5 6
 # output {'2': 2, '4': 2, '5': 2, '6': 2, '7': 1}s


freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)