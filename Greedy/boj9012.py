'''
BoJ 9012    Silver 4
괄호
'''
N = int(input())

for _ in range(N):
    paren = input()
    count = 0

    for i in paren:
        if i == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            break

    if count == 0:
        print("YES")
    else:
        print("NO")
