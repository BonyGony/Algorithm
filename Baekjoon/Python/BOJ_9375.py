testCase = int(input())
    
for i in range(testCase):
    n = int(input())
    clothesDic = {}
    result = 1
    
    for j in range(n):
        a, b = input().split()
        if b in clothesDic:
            clothesDic[b] += 1
        else:
            clothesDic[b] = 1
        
    for v in clothesDic.values():
        result *= (v+1)
    
    result -= 1
    
    print(result)