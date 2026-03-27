t = (1, 2, 3, 4, 5, 6, 7, 8)

# Using tuple comprehensions (store results in tuples)
even = tuple(x for x in t if x % 2 == 0)
odd = tuple(x for x in t if x % 2 != 0)

print("Even elements:", even)
print("Odd elements:", odd)