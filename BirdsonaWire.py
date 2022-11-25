#greedy
l, d, n = (int(x) for x in input().split())
if n == 0:
    print((l-12)//d + 1)
else:
    birds = []
    for _ in range(n):
        birds.append(int(input()))
    birds.sort()
    
    pos = 6
    count = 0
    for bird in birds:
        while pos + d <= bird:
            count += 1
            pos += d
        pos = bird + d
    while pos <= (l-6):
        count += 1
        pos += d
    print(count)