from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

def makeZero(arr, n):
    
    ar = deepcopy(arr)
    ar.append(str(n))

    if len(ar) == (N+N-1):
        s = ''.join(ar).replace(" ", "")
        if eval(s) == 0:
            answer.append(''.join(ar))
        return

    ar.append(' ')
    makeZero(ar, n+1)
    ar.pop()
    
    ar.append('+')
    makeZero(ar, n+1)
    ar.pop()
    
    ar.append('-')
    makeZero(ar, n+1)
    ar.pop()


testCase = int(input())

for _ in range(testCase):
    
    N = int(input())

    answer = []

    makeZero([], 1)

    for i in range(len(answer)):
        print(answer[i])
    print()