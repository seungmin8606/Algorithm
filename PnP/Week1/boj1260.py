'''
BoJ 1260    Silver 2
DFS와 BFS
'''

import sys
from collections import deque


def DFS(v):
    visited[v] = True
    DFSlist.append(v)
    for i in range(len(graph[v])):
        j = graph[v][i]
        if visited[j] == False:
            DFS(j)


def BFS(v):
    visited[v] = True
    BFSlist.append(v)
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        for i in range(len(graph[x])):
            j = graph[x][i]
            if visited[j] == False:
                visited[j] = True
                queue.append(j)
                BFSlist.append(j)


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

DFSlist = []
BFSlist = []

visited = [False] * (N+1)
visited[0] = True
DFS(V)
print(' '.join(str(i) for i in DFSlist))

visited = [False] * (N+1)
visited[0] = True
BFS(V)
print(' '.join(str(i) for i in BFSlist))
