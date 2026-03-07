def show_num(*args):
    total = 0
    for num in args :
        total += num
    return total

print(show_num(1,2,3,4))
