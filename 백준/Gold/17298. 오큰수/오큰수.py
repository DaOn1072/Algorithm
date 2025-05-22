import sys
n = int(input())
ans = [0] * n # 정답 리스트
A = list(map(int, input().split())) # 수열 리스트 채우기
myStack = [] #스택 선언

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
        ans[myStack.pop()] = A[i] # 오큰수를 현재 수열로 정답 리스트에 저장하기
    myStack.append(i)
  
while myStack: # 반복문이 끝났는 데도 스택에 값이 남아있다면, 빌 때까지 반복
    ans[myStack.pop()] = -1 # 스택에 쌓인 index에 -1을 넣기
    
for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")