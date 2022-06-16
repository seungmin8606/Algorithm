'''
BoJ 13458   Bronze 2
시험 감독
'''
N = int(input())
num = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0

for i in num:
    rest = i - B
    count += 1
    if rest > 0:
        count += (rest // C)
        if rest % C:
            count += 1

print(count)
