
def cn_w(text):
    v = "aeiou"
    text = text.lower()
    we = {}

    for w in text:
        if w in v:
            we[w]=we.get(w,0)+1
        
    return we

text = ("Hello World")
print(cn_w(text))
