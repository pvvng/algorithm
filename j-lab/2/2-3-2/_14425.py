import sys
input = sys.stdin.readline

def sol(S:set, chekcs: list):
  cnt = 0
  for e in chekcs:
    if e in S:
      cnt += 1
  return cnt

N, M = map(int, input().split())
S = set(input() for _ in range(N))
checks = [input() for _ in range(M)]
print(sol(S, checks))