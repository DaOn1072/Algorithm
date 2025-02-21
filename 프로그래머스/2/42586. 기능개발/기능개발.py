from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for p, s in zip(progresses, speeds):
        queue.append((100-p+s-1)//s)
        
    while queue:
        devlop_day = queue.popleft()
        cnt = 1
        
        while queue and queue[0] <= devlop_day:
            queue.popleft()
            cnt += 1
        
        answer.append(cnt)
        
    return answer