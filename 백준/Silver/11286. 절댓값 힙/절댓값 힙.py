from queue import PriorityQueue  # 우선순위 큐 자료구조를 사용하기 위해 import
import sys

print = sys.stdout.write  
input = sys.stdin.readline 

N = int(input())  # 입력받을 명령의 개수
myQueue = PriorityQueue()  # 우선순위 큐 생성

for i in range(N):
    request = int(input())  # 각 명령 입력받음
    if request == 0:
        if myQueue.empty():  # 큐가 비어있으면
            print('0\n')  # 0 출력
        else:
            temp = myQueue.get()  # 우선순위가 가장 높은(절댓값이 가장 작은) 값 추출
            print(str((temp[1])) + '\n')  # 원래 숫자(request)를 출력
    else:
        # 절댓값을 기준으로 정렬. 같은 절댓값이면 원래 숫자 값 기준(음수 우선)
        myQueue.put((abs(request), request))  # 튜플로 저장: (절댓값, 원래값)
