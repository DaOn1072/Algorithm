import heapq

def solution(scoville, K):
    answer = 0
    mix_scoville = 0
    # 1. scoville 리스트를 heapq로 변환
    heapq.heapify(scoville)
    
    # 2. scoville 0번째 값이 K 기준에 적합한지
    while scoville[0] < K:
        # 2-1. scoville의 길이가 1을 초과하지 못하면 비교 수가 없으므로 -1 return
        if len(scoville) < 2:
            return -1
        
        # 2-2. scoville의 가장 작은 수와 두번째 작은 수 * 2 구하기
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        # 2-3. scoville에 mix_scoville 추가하기
        heapq.heappush(scoville, mix_scoville)
        answer +=1    
    return answer