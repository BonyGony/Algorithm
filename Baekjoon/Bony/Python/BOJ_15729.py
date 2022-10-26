def checkRange(i):
    if i >= 0 and i < n:
        return True
    else:
        return False

def clickButton(index):
    global startButtons
    
    for i in range( index, index+3 ):
        if checkRange(i):
            startButtons[i] = not startButtons[i]

def makeTargetButton():
    cnt = 0
    
    for i in range(n):
        if targetButtons[i] != startButtons[i]:
            cnt += 1
            clickButton(i)
            
    return cnt

n = int(input())
startButtons = [0]*n
targetButtons = list(map(int, input().split()))

print(makeTargetButton())

