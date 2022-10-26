N = int(input())
arr = [1,5,10,50]
numSet = set()

def find(sum,i, k):
    if i==0:
        numSet.add(sum)
        return
    for j in range(k,len(arr)):
            find(sum+arr[j], i-1,j)


find(0,N,0)

print(len(numSet))