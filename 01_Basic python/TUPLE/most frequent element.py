t = (1, 2, 3, 2, 4, 2, 5, 3)

# Find the most frequent element
most_freq = max(t, key=t.count)

print("Tuple:", t)
print("Most frequent element:", most_freq)