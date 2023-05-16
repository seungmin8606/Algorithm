'''
BoJ 1931    Silver 1    greedy
회의실 배정
'''

N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: (x[1], x[0]))

count = 1
j = 0
for i in range(1, N):
    if schedule[i][0] >= schedule[j][1]:
        count += 1
        j = i

print(count)
