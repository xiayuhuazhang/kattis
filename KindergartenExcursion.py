#tricky ideas
s= input()
x, y  = 0,0
#record frequency of 0,1,2
fre = [0,0,0]
res = 0
for char in s:
    if char != '0':
        fre[int(char)] += 1
    for y in range(2, int(char), -1):
        res += fre[y]
print(res)