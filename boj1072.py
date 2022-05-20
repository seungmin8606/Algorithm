'''
BoJ 1072    Silver 3
'''
X, Y = map(int, input().split())

Z = Y * 100 // X
newZ = Z
answer = 0

if Z >= 99:
    answer = -1
else:
    start = 1
    end = X

    while start <= end:
        M = (start + end) // 2
        if (Y + M) * 100 // (X + M) <= Z:
            start = M + 1
        else:
            answer = M
            end = M - 1

print(answer)
