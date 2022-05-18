'''
BoJ 2644    Silver 2    Graph
'''
from collections import deque


def BFS(a, b):
    visited[a] = True
    queue = deque()
    queue.append(a)
    while queue:
        x = queue.popleft()
        n = len(child[x])
        if n != 1:
            for i in range(1, n):
                y = child[x][i]
                if not visited[y]:
                    visited[y] = True
                    dist[y] = dist[x] + 1
                    queue.append(y)
        if parent[x][0] != 0:
            y = parent[x][0]
            if not visited[y]:
                visited[y] = True
                dist[y] = dist[x] + 1
                queue.append(y)
        if dist[b] != 0:
            return dist[b]
    if dist[b] == 0:
        return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())

child = [[0] for _ in range(n+1)]
parent = [[0] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    child[x].append(y)

    parent[y] = [x]

dist = [0] * (n+1)
visited = [False] * (n+1)

answer = BFS(a, b)

print(answer)
