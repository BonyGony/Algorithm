import re

sArr = list(input())
pattern = re.compile('\d')

alphabetArr = []
num = 0

for ch in sArr:
    if re.match(pattern, ch):
        num += int(ch)
    else:
        alphabetArr.append(ch)

alphabetArr.sort()

print(''.join(alphabetArr) + str(num))
