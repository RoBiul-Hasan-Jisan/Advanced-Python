def show_num(*args):
    total = 0
    for num in args :
        total += num
    return total
nums = list(map(int,input("enter number :").split()))
print(show_num(*nums))
