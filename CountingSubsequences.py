n = int(input())
while n > 0:
    space = input()
    length = int(input())
    sum_, count = 0, 0
    dic = {0:1}
    ls = input().split()
    for i in ls:
        sum_ += int(i)
        count += dic.get(sum_ - 47, 0)
        dic[sum_] = 1 + dic.get(sum_, 0)
    print(count)
    n -= 1