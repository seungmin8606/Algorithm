'''
BoJ 20055   Gold 5  implementation
'''
N, K = map(int, input().split())
durability = list(map(int, input().split()))
robot = [0] * N

step = 0

while durability.count(0) < K:
    durability.insert(0, durability.pop())  # 1.회전
    robot.insert(0, robot.pop())            # 1.회전

    if robot[N-1] != 0:
        robot[N-1] = 0

    for i in range(N-1, -1, -1):
        if robot[i] == 1:
            if durability[i+1] > 0 and robot[i+1] == 0:
                robot[i] = 0
                robot[i+1] = 1
                durability[i+1] -= 1

    if robot[N-1] != 0:
        robot[N-1] = 0

    if durability[0] > 0:
        robot[0] = 1
        durability[0] -= 1
    step += 1

print(step)
