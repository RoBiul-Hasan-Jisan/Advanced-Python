from collections import Counter

text = "Hello hello world"

text = text.replace(" ","").lower()

re = dict(Counter(text))

print(re)

# M-2

def cnt(text):
    wd = text.loewer().split()
    wc = {}

    for w in wd:
        if w in wc:
            wc[w]=+1
        else:
            wc[w]=1

text = ("he he kk he kk sd")
print(cnt(text))

