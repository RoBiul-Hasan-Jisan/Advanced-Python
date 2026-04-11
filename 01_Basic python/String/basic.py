# Create a string
s = "  Python Programming  "
print("Original string:", s)

# 1. Access characters
print("First character:", s[0])
print("Last character:", s[-1])

# 2. Slice string
print("Substring (index 2 to 8):", s[2:9])
print("From start to index 5:", s[:6])
print("From index 7 to end:", s[7:])

# 3. Check if substring exists
print("Contains 'Python'?", 'Python' in s)
print("Contains 'Java'?", 'Java' in s)

# 4. Length of string
print("Length:", len(s))

# 5. Case conversion
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())  # Capitalize first letter of each word
print("Swap case:", s.swapcase()) # Upper <-> Lower

# 6. Remove spaces
print("Strip:", s.strip())   # Remove leading/trailing
print("Lstrip:", s.lstrip()) # Remove leading spaces
print("Rstrip:", s.rstrip()) # Remove trailing spaces

# 7. Replace substring
print("Replace 'Python' with 'Java':", s.replace("Python", "Java"))

# 8. Concatenate strings
s2 = " is fun!"
print("Concatenated:", s + s2)

# 9. Repeat string
print("Repeated:", "Hello! " * 3)

# 10. Split and join
words = s.split()  # Split by spaces
print("Split words:", words)
joined = "-".join(words)
print("Joined with '-':", joined)

# 11. Count occurrences
print("Count of 'm':", s.count('m'))

# 12. Find substring index
print("Index of 'Python':", s.find("Python"))  # Returns -1 if not found

# 13. Check start/end
print("Starts with 'Python'?", s.strip().startswith("Python"))
print("Ends with 'Programming'?", s.strip().endswith("Programming"))

# 14. Check if string is alphanumeric, alphabetic, digits
print("Is alphanumeric?", s.strip().isalnum())
print("Is alphabetic?", s.strip().isalpha())
print("Is digit?", "123".isdigit())