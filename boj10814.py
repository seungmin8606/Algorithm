'''
BoJ 10814   Silver 5
나이순 정렬
'''
N = int(input())
member = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    member.append([age, name])

member.sort(key=lambda x: x[0])

for i in range(N):
    print(member[i][0], member[i][1])
