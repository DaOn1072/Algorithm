def solution(answers):
    answer = []
    p1= [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1, score2, score3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score1 += 1
        if answers[i] == p2[i % len(p2)]:
            score2 += 1
        if answers[i] == p3[i % len(p3)]:
            score3 += 1
    
    max_score = max(score1, score2, score3)

    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
    return answer