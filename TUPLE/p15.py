t = (1, 2, 3, 4, 5)

product = 1  # Start with 1 because multiplying by 0 will make everything 0
for x in t:
    product *= x

print("Product of all elements:", product)