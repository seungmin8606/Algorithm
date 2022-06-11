'''
BoJ 16234   Gold 5  Graph
인구 이동
'''
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    global answer, visited
    result = 1
    while result:
        result = BFSAll()
        answer += result
        visited = [[False] * N for _ in range(N)]
    return answer


def BFSAll():
    global popul, qu
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                qu = deque()
                qu.append([i, j])
                queue.append([i, j, popul[i][j]])
                A, B = BFS()
                if A == 1:
                    continue
                result = 1
                aver = B // A
                for tmp in qu:
                    popul[tmp[0]][tmp[1]] = aver
    return result


def BFS():
    union_cnt = 0
    union_sum = 0
    while queue:
        temp = queue.popleft()
        popu = temp[2]
        union_cnt += 1
        union_sum += popu
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                k = popul[nx][ny]
                if (popu - R <= k <= popu - L or popu + L <= k <= popu + R) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, k])
                    qu.append([nx, ny])
    return union_cnt, union_sum


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().rstrip().split())
visited = [[False] * N for _ in range(N)]
popul = []

for _ in range(N):
    popul.append(list(map(int, input().rstrip().split())))

answer = 0
queue = deque()
qu = deque()

print(solve())
