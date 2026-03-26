# Create a dictionary of 5 students with marks and print each student with marks.
text = input("k:v separatre using , :")

text = {k: int(v) for k, v in ( item.split(":") for item in text.split(","))}

print(text)

# Example Output:
# Rahim -> 80
# Karim -> 75