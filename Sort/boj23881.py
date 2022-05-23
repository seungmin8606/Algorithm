'''
BoJ 23881   Bronze 1    Sort
알고리즘 수업 - 선택 정렬 1
'''
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(N-1, -1, -1):
    max_index = i
    for j in range(i):
        if arr[j] > arr[max_index]:
            max_index = j
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        count += 1
    if count == K:
        print(arr[max_index], arr[i])
        break

if count < K:
    print(-1)
