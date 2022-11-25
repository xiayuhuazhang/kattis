#use try-except to deal with uncertain input lines
try:
    case = 1
    while True:
        n = int(input())
        print("Case {}:".format(case))
        ls = []
        for _ in range(n):
            ls.append(int(input()))
        sums = set()
        for i in range(n-1):
            for j in range(i+1,n):
                sums.add(ls[i] + ls[j])
        lsums = list(sums)
        q = int(input())
        for _ in range(q):
            num = int(input())
            diff = float("inf")
            for k in range(len(lsums)):
                if abs(lsums[k] - num) < diff:
                    diff = abs(lsums[k] - num)
                    loc = k
            print("Closest sum to {} is {}.".format(num,lsums[loc]))
        case += 1
except EOFError:
    pass