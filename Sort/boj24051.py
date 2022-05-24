'''
BoJ 24051   Bronze 1    Sort
알고리즘 수업 - 삽입 정렬 1
'''
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, N):
    index = i - 1
    temp = arr[i]
    while index >= 0 and temp < arr[index]:
        arr[index+1] = arr[index]
        count += 1
        if count == K:
            print(arr[index+1])
            break
        index -= 1
    if index + 1 != i:
        arr[index+1] = temp
        count += 1
        if count == K:
            print(temp)
            break

if count < K:
    print(-1)
