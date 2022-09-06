n = int(input())

wines = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    wines[i] = int(input())

if n >= 1:
    dp[1] = wines[1]
if n >= 2:
    dp[2] = wines[1] + wines[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+wines[i]+wines[i-1], dp[i-2]+wines[i], dp[i-1])

print(dp[n])
