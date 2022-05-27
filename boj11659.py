'''
BoJ 11659   Silver3
구간 합 구하기 4
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
number = list(map(int, sys.stdin.readline().rstrip().split()))
prefix = [0]
sum = 0

for i in number:
    sum += i
    prefix.append(sum)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer = prefix[b] - prefix[a-1]
    print(answer)
