# 필요한 리스트와 변수 초기화
checkList = [0] * 4     # 각 DNA 문자의 최소 요구 개수를 저장하는 리스트 (A, C, G, T 순)
myList = [0] * 4        # 현재 윈도우 내 각 문자 개수를 저장하는 리스트
checkSecret = 0         # 4개의 문자 조건 중 현재 만족한 조건의 개수

# 새로 들어온 문자를 처리하는 함수
def myadd(c):
    global checkList, myList, checkSecret
    # 문자 c가 'A'일 경우
    if c == 'A':
        myList[0] += 1  # 현재 윈도우에서 'A' 개수 증가
        if myList[0] == checkList[0]:  # 요구 조건과 일치할 경우
            checkSecret += 1          # 조건 만족 개수 증가
    # 문자 c가 'C'일 경우
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    # 문자 c가 'G'일 경우
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    # 문자 c가 'T'일 경우
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 제거되는 문자를 처리하는 함수
def myremove(c):
    global checkList, myList, checkSecret
    # 문자 c가 'A'일 경우
    if c == 'A':
        if myList[0] == checkList[0]:  # 현재 개수가 조건을 만족했었다면
            checkSecret -= 1          # 조건을 더 이상 만족하지 않게 되므로 감소
        myList[0] -= 1                # 문자 개수 감소
    # 문자 c가 'C'일 경우
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    # 문자 c가 'G'일 경우
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    # 문자 c가 'T'일 경우
    elif c == 'T':
        if myList[3] == checkList[3]: 
            checkSecret -= 1
        myList[3] -= 1

# 문자열의 길이 S, 부분 문자열의 길이 P 입력 받기
S, P = map(int, input().split())
Result = 0  # 최종 결과 저장할 변수 (조건을 만족하는 부분 문자열 개수)
A = list(input())  # DNA 문자열 입력 받아 리스트로 변환
checkList = list(map(int, input().split()))  # 각 문자에 대한 최소 요구 개수

# checkList의 값이 0이면, 해당 조건은 이미 만족한 것으로 간주
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 윈도우(P 길이만큼)의 문자들 추가
for i in range(P):
    myadd(A[i])  # 문자 하나씩 추가하며 상태 업데이트

# 초기 윈도우가 조건을 만족하는지 확인
if checkSecret == 4:
    Result += 1

# 슬라이딩 윈도우 이동: 윈도우를 한 글자씩 앞으로 옮기며 검사
for i in range(P, S):
    j = i - P           # 제거할 문자 위치
    myadd(A[i])         # 새로 들어온 문자 추가
    myremove(A[j])      # 옛날 문자 제거
    if checkSecret == 4:  # 조건을 모두 만족하면 결과 증가
        Result += 1

# 조건을 만족하는 부분 문자열의 개수 출력
print(Result)
