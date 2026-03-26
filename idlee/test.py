rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

rows = 5
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "*"*i)


for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()


rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "*"*i)


rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "*"*(2*i-1))


rows = 5
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "*"*(2*i-1))

rows = 5
# Top Pyramid
for i in range(1, rows+1):
    print(" "*(rows-i) + "*"*(2*i-1))
# Bottom inverted Pyramid
for i in range(rows-1, 0, -1):
    print(" "*(rows-i) + "*"*(2*i-1))





rows = 5
for i in range(1, rows+1):
    if i == 1:
        print(" "*(rows-i) + "*")
    elif i == rows:
        print("*"*(2*rows-1))
    else:
        print(" "*(rows-i) + "*" + " "*(2*i-3) + "*")














    

