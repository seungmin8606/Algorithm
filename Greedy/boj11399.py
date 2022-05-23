'''
BoJ 11399   Silver 3    Greedy
ATM
'''
import sys

N = int(sys.stdin.readline())
minute = list(map(int, sys.stdin.readline().split()))
minute.sort()

sum, answer = 0, 0

for i in range(N):
    sum += minute[i]
    answer += sum

print(answer)
