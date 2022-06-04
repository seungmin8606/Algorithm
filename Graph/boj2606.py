'''
BoJ 2606    Silver 3    Graph
바이러스
'''
from collections import deque


def BFS():
    global count
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        idx = queue.popleft()
        count += 1
        for i in node[idx]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


C = int(input())
N = int(input())

node = [[] for _ in range(C+1)]

for _ in range(N):
    i, j = map(int, input().split())
    node[i].append(j)
    node[j].append(i)

visited = [False] * (C+1)
count = -1

BFS()

print(count)
