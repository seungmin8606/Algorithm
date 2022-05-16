'''
BoJ 1012    Silver 3    Graph
'''
import sys
sys.setrecursionlimit(10000)


def DFSAll(N, M):
    global count
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and not visited[i][j]:
                DFS(i, j)
                count += 1


def DFS(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if ground[nx][ny] == 1 and not visited[nx][ny]:
                DFS(nx, ny)


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        ground[b][a] = 1
    count = 0
    DFSAll(N, M)
    print(count)
