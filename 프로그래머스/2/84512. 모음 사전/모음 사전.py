from itertools import product

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    dict = []
    
    for i in range(5):
        for v in product(vowels, repeat = i+1):
            dict.append(''.join(v))
            
    dict.sort()
    return dict.index(word)+1