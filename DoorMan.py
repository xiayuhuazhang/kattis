#interesting idea
x = int(input())
#women 1 and man -1
line = [1 if p =="W" else -1 for p in input()]
sum_ = 0
count = 0
for i in line:
    sum_ += i
    count += 1
    if abs(sum_) == x + 2:
        break
#break-- same gender after abs == x    
if count < len(line):
    print(count-2)
    
#finish the whole line
elif abs(sum_) == x+1:
    print(count-1)
else:
    print(count)