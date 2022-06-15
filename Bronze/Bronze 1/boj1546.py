N = int(input())

score = list(map(int, input().split()))

sum = 0

for i in range(N):
    sum += score[i]

answer = sum / max(score) / N * 100
print(answer)
