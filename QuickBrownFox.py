#checking the missing words in sentences
import string
import re

lines = [input() for _ in range(int(input()))]
alpha = set(string.ascii_lowercase)
for line in lines:
    temp = re.sub('[^a-zA-Z]+', '', line).lower()
    num = set(temp)
    if len(num) == 26:
        print("pangram")
    else:
        print("missing", ''.join(sorted(alpha.difference(num))))