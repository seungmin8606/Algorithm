'''
BoJ 15650   Silver 3    Backtracking
N과 M(2)
'''
import sys


def solve(A, x):
    if len(A) == M:
        print(' '.join(map(str, A)))
        return

    for i in range(x, N):
        if num[i] not in A:
            A.append(num[i])
            solve(A, i)
            A.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
num = [i for i in range(1, N+1)]

for i in num:
    answer = [i]
    solve(answer, i)
