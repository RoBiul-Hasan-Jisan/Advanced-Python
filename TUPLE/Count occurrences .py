# Count how many times an element appears in a tuple

t = list(map(int, input("Enter tuple elements: ").split()))

# Count occurrences in one line
count_dict = {x: t.count(x) for x in t}

print(count_dict)