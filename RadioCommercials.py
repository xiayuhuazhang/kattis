nums, price = list(map(int,input().split()))
ls = list(map(lambda x: int(x)- price ,input().split()))
cursum = 0 
maxsum = 0
for n in ls:
    cursum = max(0, cursum +n)
    maxsum = max(maxsum, cursum)
print(maxsum)