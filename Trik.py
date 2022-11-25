move = list(input())
def change(ls,a,b):
    ls[a], ls[b] = ls[b], ls[a]
    return 
ls = [True, False, False]
for s in move:
    if s == 'A':
        change(ls,0,1)
    elif s =='B':
        change(ls,1,2)
    else:
        change(ls,0,2)

for i in range(3):
    if ls[i]:
        print(i+1)