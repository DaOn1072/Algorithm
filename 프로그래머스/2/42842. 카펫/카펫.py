def solution(brown, yellow):
    answer = []
    yellow_w = 0
    yellow_h = 0
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_w = yellow // i
            yellow_h = i
            
            if (yellow_w * 2) + (yellow_h * 2) + 4 == brown:
                answer.append(yellow_w + 2)
                answer.append(yellow_h + 2)
                
                return answer
    return answer