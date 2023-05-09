'''
BoJ 1018    Silver 4
체스판 다시 칠하기
'''


def count(board):
    cnt_B, cnt_W = 0, 0
    # 맨 왼쪽 위 칸 검정색
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[i][j] == 'W':
                    cnt_B += 1
            else:
                if board[i][j] == 'B':
                    cnt_B += 1
    # 맨 왼쪽 위 칸 흰색
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[i][j] == 'B':
                    cnt_W += 1
            else:
                if board[i][j] == 'W':
                    cnt_W += 1
    return min(cnt_B, cnt_W)


N, M = map(int, input().split())
Board = []
answer = 64

for _ in range(N):
    Board.append(input())

for i in range(N-7):
    for j in range(M-7):
        answer = min(answer, count([row[j:j+8] for row in Board[i:i+8]]))
    if answer == 0:
        break

print(answer)
