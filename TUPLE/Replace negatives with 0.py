t = (4, -2, 7, -5, 0, 3, -1)

# Replace negatives with 0
t_no_neg = tuple(x if x >= 0 else 0 for x in t)

print("Original tuple:", t)
print("Tuple with negatives replaced:", t_no_neg)