'''
BoJ 23968   Bronze 1    Sort
알고리즘 수업 - 버블 정렬 1
'''
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(N-1, -1, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1
        if count == K:
            print(arr[j], arr[j+1])
            break
    if count == K:
        break

if count < K:
    print(-1)
