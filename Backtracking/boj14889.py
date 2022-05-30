'''
BoJ 14889   Silver 2    Backtracking
스타트와 링크
'''
import sys
input = sys.stdin.readline


def backtracking(length, idx):
    global answer
    if length == N//2:
        start_sum = 0
        link_sum = 0
        for i in range(N):
            for j in range(N):
                if start[i] and start[j]:
                    start_sum += stat[i][j]
                if not start[i] and not start[j]:
                    link_sum += stat[i][j]
        sub = abs(start_sum - link_sum)
        answer = min(answer, sub)
        return

    for i in range(idx, N):
        if not start[i]:
            start[i] = True
            backtracking(length+1, i+1)
            start[i] = False


N = int(input().rstrip())
stat = []

for _ in range(N):
    stat.append(list(map(int, input().rstrip().split())))

start = [False for _ in range(N)]

answer = float('inf')
backtracking(0, 0)

print(answer)
