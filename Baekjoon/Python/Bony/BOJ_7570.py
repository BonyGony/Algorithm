import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)
positions = [0] * (n+1)

for i in range(1, n+1):
    positions[nums[i]] = i

count = 1
max = -1

for i in range(1, len(nums)-1):
    if (positions[i] < positions[i+1]):
        count += 1
        if (count > max):
            max = count
    else:
        count = 1

print(n-max)
