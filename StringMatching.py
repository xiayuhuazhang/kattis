#kmp
import sys

def match_table(pattern):
    length = len(pattern)
    cur = 0
    table = [0] * length
    if length == 1:
        return table

    for i, char in enumerate(pattern[1:], 1):
        while cur > 0 and pattern[cur] != char:
            cur = table[cur - 1]
        if pattern[cur] == char:
            cur += 1
        table[i] = cur
    return table

def kmp(s, pattern):

    table = match_table(pattern)
    sl = len(s)
    pl = len(pattern)

    begin = 0
    s_index = 0
    p_index = 0
    match = []

    while sl - begin > pl:
        
        while p_index < pl and s[s_index] == pattern[p_index]:
            s_index += 1
            p_index += 1

        if p_index >= pl:
            match.append(str(begin))
            
        if p_index > 0 and table[p_index - 1] > 0:
            begin = s_index - table[p_index - 1]
            p_index = table[p_index - 1]

        else:
            if s_index == begin:
                s_index += 1
            begin = s_index
            if p_index > 0:
                p_index = table[p_index - 1]

    if s[-pl:] == pattern:
        match.append(str(len(s) - pl))
    print(' '.join(match))

s = ''
pattern = ''
ready = False

for line in sys.stdin:
    if not ready:
        pattern = line.rstrip('\n')
        ready = True
    else:
        s = line.rstrip('\n')
        ready = False
        kmp(s, pattern)