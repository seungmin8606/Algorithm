'''
BoJ 3190    Gold 5  implementation
'''
N = int(input())

Board = [[1] * (N+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        Board[i][j] = 0

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    Board[a][b] = 'a'

L = int(input())
X = []
D = []
for _ in range(L):
    x, d = input().split()
    X.append(int(x))
    D.append(d)

second = 1
direction = 2  # 1: 위쪽, 2: 오른쪽, 3: 아래쪽, 4: 왼쪽
snake = [(1, 1)]
nRow = 1
nCol = 2
next = Board[nRow][nCol]

while next != 1:
    if next == 0:
        snake.append((nRow, nCol))
        if (nRow, nCol) in snake[:-1]:
            break
        snake.pop(0)
    elif next == 'a':
        snake.append((nRow, nCol))
        if (nRow, nCol) in snake[:-1]:
            break
        Board[nRow][nCol] = 0

    if second in X:
        idx = X.index(second)
        d = D[idx]
        if d == "L":
            direction -= 1
        elif d == "D":
            direction += 1
        if direction == 0:
            direction = 4
        if direction == 5:
            direction = 1

    if direction == 1:
        nRow -= 1
    elif direction == 2:
        nCol += 1
    elif direction == 3:
        nRow += 1
    elif direction == 4:
        nCol -= 1

    next = Board[nRow][nCol]
    second += 1

print(second)
