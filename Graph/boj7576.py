'''
BoJ 7576    Gold 5  Graph
토마토
'''
from collections import deque


def BFS():
    while queue:
        tmp = queue.popleft()
        count = tmp[2]
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if storage[nx][ny] == 0:
                    queue.append([nx, ny, count + 1])
                    storage[nx][ny] = count + 1
    for i in range(N):
        for j in range(M):
            if storage[i][j] == 0:
                count = -1
    return count


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
storage = []
for _ in range(N):
    storage.append([i for i in map(int, input().split())])

queue = deque()
count = 0

for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            queue.append([i, j, 0])

print(BFS())
