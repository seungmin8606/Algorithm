'''
BoJ 1263    Silver 1
시간 관리
'''
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

schedule.sort(key=lambda x: (x[1], x[0]), reverse=True)

temp = schedule[0][1]

for i in range(N):
    if temp > schedule[i][1]:
        temp = schedule[i][1]
    temp -= schedule[i][0]

if temp < 0:
    temp = -1

print(temp)
