'''
BoJ 84165   Gold 5
AC
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    reversed = False
    iserror = False
    p = input()
    n = int(input())
    s = input().strip()
    if n > 0:
        a = deque(map(int, s[1:-1].split(',')))
    else:
        a = deque()

    for i in p:
        if i == 'R':
            if reversed:
                reversed = False
            else:
                reversed = True
        elif i == 'D':
            if len(a) == 0:
                iserror = True
                break
            if reversed:
                a.pop()
            else:
                a.popleft()

    if iserror:
        print("error")
    else:
        if reversed:
            a.reverse()
        li = list(a)
        temp = ''.join(str(li))
        temp = temp.replace(' ', '')
        print(temp)
