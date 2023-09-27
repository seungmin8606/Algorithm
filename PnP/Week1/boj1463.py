'''
BoJ 1463    Silver 3
1로 만들기
'''

N = int(input())

if N < 4:
    count = [0, 0, 1, 1]
else:
    count = [0] * (N + 1)
    count[2] = 1
    count[3] = 1
    for i in range(4, N+1):
        if i % 6 == 0:
            a = min(count[i//3], count[i//2], count[i-1])
            count[i] = a + 1
        elif i % 3 == 0:
            a = min(count[i//3], count[i-1])
            count[i] = a + 1
        elif i % 2 == 0:
            a = min(count[i//2], count[i-1])
            count[i] = a + 1
        else:
            a = count[i-1]
            count[i] = a + 1

print(count[N])
