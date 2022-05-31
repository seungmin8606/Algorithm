'''
BoJ 9663    Gold 5  Backtracking
N-Queen
'''


def N_queen(k):
    global count
    if k == N:
        count += 1
        return

    for c in range(N):
        if can(k, c):
            queen[k] = c
            N_queen(k+1)


def can(k, c):
    if k == 0:
        return True
    add = k + c
    sub = k - c
    for i in range(k):
        if queen[i] == c:
            return False
        elif i + queen[i] == add:
            return False
        elif i - queen[i] == sub:
            return False
    return True


N = int(input())

count = 0
queen = [-1 for _ in range(N)]
N_queen(0)

print(count)
