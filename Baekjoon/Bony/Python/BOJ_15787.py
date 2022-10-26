import sys
from collections import deque

def commandOrder(orderNum, trainNum, seatNum = 1 ):
    if orderNum == 1:
        trains[trainNum][seatNum] = 1
    elif orderNum == 2:
        trains[trainNum][seatNum] = 0
    elif orderNum == 3:
        trains[trainNum].rotate(1)
        trains[trainNum][0] = 0
    elif orderNum == 4:
        trains[trainNum].rotate(-1)
        trains[trainNum][19] = 0

def findTrainRecord():
    information = []
    
    for train in trains:
        if train not in information:
            information.append(train)
    
    return len(information)

n, m = map(int, input().split(" "))
trains = [deque([0]*20) for _ in range(n)]

for _ in range(m):
    inputs = list(map(int, input().split(" ")))
    if len(inputs) == 2:
        orderNum, trainNum = inputs
        commandOrder(orderNum, trainNum-1)
    else:
        orderNum, trainNum, seatNum = inputs
        commandOrder(orderNum, trainNum-1, seatNum-1)
    
        
print(findTrainRecord());