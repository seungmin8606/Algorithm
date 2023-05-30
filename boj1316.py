'''
BoJ 1316    Silver 5
그룹 단어 체커
'''
N = int(input())
count = 0

for _ in range(N):
    word = input()

    isGroup = True
    check = []
    temp = word[0]
    for i in word:
        if i not in check:
            check.append(i)
        else:
            if i in check and i != temp:
                isGroup = False

        temp = i

    if isGroup:
        count += 1

print(count)
