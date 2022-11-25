for _ in range(int(input())):
    n = int(input())
    uni = [input() for _ in range(n)]
    uni.sort()
    flag =False
    for i in range(1, n):
        #if conflict, startswith should be true
        if uni[i].startswith(uni[i-1]):
            flag = True
    if flag:
        print('NO')
    else:
        print('YES')