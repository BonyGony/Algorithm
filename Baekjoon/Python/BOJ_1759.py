import sys
sys.setrecursionlimit(10000)

def findCollection(s):
    collectionNum, consonantNum = 0, 0
    
    for ch in s:
        if ch in collection:
            collectionNum += 1
        else:
            consonantNum += 1
            
    return collectionNum >=1 and consonantNum >= 2

def dfs(s, depth, i):
    if depth == n and findCollection(s):
        print(s)
        
    for c in range(i, len(inputs)):
        dfs(s+inputs[c], depth+1, c+1)

collection = set(['a','e','i','o','u'])

n, l = map(int, input().split(" "))
inputs = list(input().split(" "))

answer = []

inputs.sort()

dfs('', 0, 0);
