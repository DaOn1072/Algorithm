from itertools import permutations

def solution(numbers):
    answer = []
    nums = [n for n in numbers]

    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))

    for i in range(len(per)):
        per[i] = "".join(per[i])
    
    int_per = list(map(int, per))
    
    for n in int_per:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check == True:
            answer.append(n)

    return len(set(answer))