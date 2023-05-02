'''
BoJ 2805    Silver 2
나무 자르기
'''


def solve(trees, start, end, target):
    result = 0
    while True:
        mid = (start + end) // 2
        sum = 0

        for k in trees:
            if k > mid:
                sum += k - mid

        if sum == target:
            return mid
        elif start > end:
            return result
        elif sum > target:
            result = mid
            start = mid + 1
        elif sum < target:
            end = mid - 1


N, M = map(int, input().split())
trees = list(map(int, input().split()))

Max = max(trees)

if M < Max:
    height = Max - M
else:
    height = 0

answer = solve(trees, height, Max, M)
print(answer)
