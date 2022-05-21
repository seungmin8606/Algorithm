'''
BoJ 2309    Bronze 1    Sort
일곱 난쟁이
'''
dwarf = [int(input()) for _ in range(9)]

dwarf.sort()

sum = sum(dwarf)
answer = sum - 100

for i in range(9):
    for j in range(i, 9):
        if dwarf[i] + dwarf[j] == answer:
            del dwarf[j]
            del dwarf[i]
            break
    if len(dwarf) != 9:
        break

for i in range(7):
    print(dwarf[i])
