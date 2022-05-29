'''
BoJ 10845   Silver 4
큐
'''
from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        if command[0] == "push":
            queue.append(command[1])
    else:
        command = command[0]
        if command == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
