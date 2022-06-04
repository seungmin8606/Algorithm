'''
BoJ 11727   Silver 3    DP
2xn 타일링 2
'''


def DP():
    for i in range(3, n+1):
        dp.append((dp[i-2] * 2) + dp[i-1])


n = int(input())
dp = [0, 1, 3]

if n > 2:
    DP()

print(dp[n] % 10007)
