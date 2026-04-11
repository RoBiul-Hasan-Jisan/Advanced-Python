
def cn_w(text):
    
    
    we ={}

    for w in text:
        if w.isdigit():
            we[w]=we.get(w,0)+1
        
    return we

text = "My phone number is 12341213412335446565"
print(cn_w(text))


