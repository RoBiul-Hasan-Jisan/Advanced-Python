def squares(n):
    for i in range(1, n+1):
        yield i**2

for s in squares(5):
    print(s)