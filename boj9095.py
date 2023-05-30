'''
BoJ 9095    Silver 3    DP
1, 2, 3 더하기
'''
import sys

T = int(sys.stdin.readline())
dp = [0, 1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    l = len(dp)
    if n >= l:
        for _ in range(l, n+1):
            i = len(dp)
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    print(dp[n])
