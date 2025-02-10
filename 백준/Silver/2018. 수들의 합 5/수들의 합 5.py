import sys
input = sys.stdin.readline

n = int(input())
start_index, end_index, count = 1, 1, 1
sum = 1

while end_index != n:
    if sum == n:
        end_index += 1
        count += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
        