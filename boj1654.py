'''
BoJ 1654    Silver 2
랜선 자르기
'''


def solve(start, end, N):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        if mid == 0:
            break
        for line in lines:
            count += line // mid

        if count < N:
            end = mid - 1
        else:
            start = mid + 1
    return end


K, N = map(int, input().split())

lines = []
for _ in range(K):
    lines.append(int(input()))

tmp = max(lines)

answer = solve(0, tmp, N)
print(answer)
