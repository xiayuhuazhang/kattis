# convert datetime
a = [int(x) for x in input().split(':')]
b = [int(x) for x in input().split(':')]
a_se = a[0]*3600 + a[1]*60 + a[2]
b_se = b[0]*3600 + b[1]*60 + b[2]
if b_se> a_se:
    dur = b_se - a_se
else:
    dur = b_se - a_se + 86400
hour, mins, sec = list(map(str,[dur//3600, (dur%3600)//60, dur%60]))
def add0(s):
    if len(s) ==1:
        return '0'+s
    else:
        return s
    
print(':'.join(list(map(add0,[hour, mins, sec]))))