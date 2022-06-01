'''
BoJ 1620    Silver 4
나는야 포켓몬 마스터 이다솜
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dict = {}
for i in range(N):
    pokemon = input().rstrip()
    idx = str(i + 1)
    dict[pokemon] = idx
    dict[idx] = pokemon

for _ in range(M):
    print(dict[input().rstrip()])
