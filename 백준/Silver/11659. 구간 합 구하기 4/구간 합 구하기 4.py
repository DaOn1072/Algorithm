import sys

n, m = map(int, sys.stdin.readline().split())
myList = list(map(int, sys.stdin.readline().split()))
sumList = [0]
sum = 0 

for i in myList:
    sum += i
    sumList.append(sum)
    
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(sumList[e]-sumList[s-1])
