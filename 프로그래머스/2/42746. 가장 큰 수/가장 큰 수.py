from functools import cmp_to_key

def solution(numbers):
    str_num = list(map(str, numbers))
    str_num.sort(key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
    
    answer = ''.join(str_num)
    return "0" if answer[0] == "0" else answer