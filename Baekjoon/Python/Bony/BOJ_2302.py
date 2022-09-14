n = int(input())
m = int(input())

vip = []
sit = [1, 1, 2]
ans = 1

for i in range(0, m):
    k = int(input())
    vip.append(k)

for i in range(3, 41):
    sit.append(sit[i-2]+sit[i-1])

if m >= 1:
    pre = 0

    for i in range(0, m):
        ans = ans * sit[vip[i]-1-pre]
        pre = vip[i]

    ans = ans * sit[n-pre]

else:
    ans = sit[n]

print(ans)
