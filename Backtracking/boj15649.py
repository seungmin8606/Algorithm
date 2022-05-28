'''
BoJ 15649   Silver 3    Backtracking
N과 M(1)
'''
import sys


def solve(A, X):
    if len(A) == M:
        print(' '.join(map(str, A)))
        return

    for i in num:
        if i not in A and i not in X:
            B = A[:]
            A.append(i)
            solve(A, [])
            X.append(i)
            solve(B, X)


N, M = map(int, sys.stdin.readline().rstrip().split())
num = [i for i in range(1, N+1)]

for i in num:
    answer = [i]
    cant = []
    solve(answer, cant)
