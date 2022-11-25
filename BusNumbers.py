#deal with the continus digit

n = int(input())
bus = list(map(int,input().split()))
bus.sort()
dic = dict.fromkeys(bus,1)
for i in bus:
    if i in dic and dic[i] != 0:
        x = 1
        while i+x in dic and dic[i+x] != 0:
            dic[i+x] = 0
            x += 1
        #store the continus number staring from i in dic[i]
        dic[i] = x
res = ''
sorted_dict = sorted(dic.items(), key = lambda x : x[0])
for k, v in sorted_dict:
    if v == 0:
        continue
    if v == 1:
        res += str(k)+' '
    elif v == 2:
        res += str(k)+' '
        res += str(k+1)+' '
    else:
        res += str(k) + "-" + str(k+v-1)+' '
print(res)