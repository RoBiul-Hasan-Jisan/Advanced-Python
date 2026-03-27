t1 = (1, 2, 3, 2)
t2 = (3, 4, 5, 1)

# Merge and remove duplicates
merged_unique = tuple(set(t1 + t2))

print("Merged tuple without duplicates:", merged_unique)