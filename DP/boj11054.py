'''
BoJ 11054   Silver 2    DP
가장 긴 증가하는 부분 수열
'''
N = int(input())

P = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if P[i] > P[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
