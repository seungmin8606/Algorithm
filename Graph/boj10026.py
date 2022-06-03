'''
BoJ 10026   Gold 5  Graph
적록색약
'''
import sys
from collections import deque
input = sys.stdin.readline


def BFSAll():
    global count
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                queue.append([i, j, graph[i][j]])
                BFS()
                count += 1


def BFS():
    while queue:
        temp = queue.popleft()
        color = temp[2]
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, color])


def BFSAll_RG():
    global RG_count
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                queue.append([i, j, graph[i][j]])
                BFS_RG()
                RG_count += 1


def BFS_RG():
    while queue:
        temp = queue.popleft()
        color = temp[2]
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if color == 'R' or color == 'G':
                    if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny, color])
                else:
                    if graph[nx][ny] == 'B' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny, color])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
graph = [list(input()) for _ in range(N)]

count = 0
RG_count = 0

queue = deque()
visited = [[False] * N for _ in range(N)]

BFSAll()

queue = deque()
visited = [[False] * N for _ in range(N)]

BFSAll_RG()

print(count, RG_count)
