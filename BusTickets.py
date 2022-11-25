#DP
s, p, m, n= [int(x) for x in input().split()]
days = [int(x) for x in input().split()]
#dp is the minimum price as of days[i]
dp = [0]
tail = 0
for d in days:
    #tail is the m days before day d
    while days[tail] <= d-m:
        tail += 1
    #append min of single or period
    dp.append(min(s+dp[-1], p+dp[tail]))

print(dp[-1])