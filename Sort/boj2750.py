'''
BoJ 2750    Bornze 1    Sort
수 정렬하기
'''
N = int(input())
list = []
for _ in range(N):
    list.append(int(input()))

list.sort()

for i in range(N):
    print(list[i])
