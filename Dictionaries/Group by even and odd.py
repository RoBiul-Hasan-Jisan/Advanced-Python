n = list(map(int, input("Enter numbers: ").split()))

sums = {
    'even': sum(x for x in n if x % 2 == 0),
    'odd': sum(x for x in n if x % 2 != 0)
}

print(sums)