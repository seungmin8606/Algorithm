'''
BoJ 1987    Gold 4  Graph
'''


def DFS(x, y, n):
    global count
    count = max(count, n)
    if count == 26:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not alpha[board[nx][ny]]:
                alpha[board[nx][ny]] = True
                DFS(nx, ny, n+1)
                alpha[board[nx][ny]] = False


R, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []

for i in range(R):
    board.append(list(map(lambda a: ord(a) - 65, input())))

alpha = [False] * 26
alpha[board[0][0]] = True

count = 0
DFS(0, 0, 1)

print(count)
