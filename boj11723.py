'''
BoJ 11723   Silver 5
집합
'''
import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    command = list(sys.stdin.readline().strip().split())
    opcode = command[0]
    if len(command) == 2:
        x = int(command[1])
        if opcode == 'add':
            S.add(x)
        elif opcode == 'remove':
            S.discard(x)
        elif opcode == 'check':
            print(1 if x in S else 0)
        elif opcode == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
    else:
        if opcode == 'all':
            S = set([i for i in range(1, 21)])
        elif opcode == 'empty':
            S = set()
