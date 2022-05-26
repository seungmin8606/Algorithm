'''
BoJ 7569    Gold 5  Graph
토마토
'''
from collections import deque
import sys


def BFS():
    while queue:
        tmp = queue.popleft()
        count = tmp[3]
        for i in range(6):
            nx = tmp[1] + dx[i]
            ny = tmp[2] + dy[i]
            nh = tmp[0] + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
                if storage[nh][nx][ny] == 0:
                    queue.append([nh, nx, ny, count + 1])
                    storage[nh][nx][ny] = count + 1
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if storage[z][i][j] == 0:
                    count = -1
    return count


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, sys.stdin.readline().split())
storage = []

for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append([i for i in map(int, sys.stdin.readline().split())])
    storage.append(floor)

queue = deque()
count = 0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if storage[h][i][j] == 1:
                queue.append([h, i, j, 0])

print(BFS())
