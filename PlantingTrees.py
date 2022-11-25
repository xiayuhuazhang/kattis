n = int(input())
tree = [int(x) for x in input().split()]
tree.sort(reverse=True)
#cur longest day need
long = tree[0]
#day count
day = 1
for i in range(1,n):
    long -= 1
    day += 1
    if tree[i] > long:
        long = tree[i]
day += long
print(day+1)