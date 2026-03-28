def shout(text):
    return text.upper() 

def whisper(text):
    return text.lower()  

def speak(func):
    return func("Hello")  
print(speak(shout))
print(speak(whisper))