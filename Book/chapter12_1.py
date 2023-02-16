scoreArr = list(map(int, list(input())))
mid = len(scoreArr)//2
left = scoreArr[:mid]
right = scoreArr[mid:]

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')
