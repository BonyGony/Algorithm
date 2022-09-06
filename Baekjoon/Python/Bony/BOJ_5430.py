from collections import deque

testCase = int(input())

for _ in range(testCase):
    try:
        orders = input()
        n = int(input())
        numArr = deque(input()[1:-1].split(','))
        reverse = 0

        if n == 0:
            numArr = deque([])

        for order in orders:
            if order == 'R':
                reverse += 1
            elif order == 'D':
                if len(numArr) == 0:
                    raise

                if reverse % 2 == 0:
                    numArr.popleft()
                else:
                    numArr.pop()

        if reverse % 2 == 0:
            print("[" + ",".join(numArr) + "]")
        else:
            numArr.reverse()
            print("[" + ",".join(numArr) + "]")
    except:
        print('error')
