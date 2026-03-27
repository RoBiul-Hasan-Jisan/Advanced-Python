n = list(map(int,input("Enter numer :").split()))

neg = list(x if x >= 0 else 0 for x in n)


print(neg)
