from functools import reduce
nums = list(map(int,input("enter number :").split()))

total = reduce(lambda x, y: x * y, nums)
print(total)