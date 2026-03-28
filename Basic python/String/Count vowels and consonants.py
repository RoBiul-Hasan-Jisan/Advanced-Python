text = input("Enter a string: ").lower()  # convert to lowercase
vowels = "aeiou"

v_count = sum(1 for c in text if c.isalpha() and c in vowels)
c_count = sum(1 for c in text if c.isalpha() and c not in vowels)

print("Vowels:", v_count)
print("Consonants:", c_count)