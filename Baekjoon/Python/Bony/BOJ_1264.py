import re
import sys
input = sys.stdin.readline

while True:
    s = input()
    regEx = re.compile('[aeiouAEIOU]')

    if s[0] == '#':
        break

    num = len(regEx.findall(s))
    print(num)
