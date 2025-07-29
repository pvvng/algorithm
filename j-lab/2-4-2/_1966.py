import sys
input = sys.stdin.readline

from collections import deque

def sol(docs:deque, M:int):
  cnt = 0
  while True:
    p = docs.popleft()
    exist = len(list(filter(lambda d: d[1] > p[1], docs)))
    if exist:
      docs.append(p)
      continue # cnt 증가 x
    cnt += 1
    if p[0] == M: # 종료 조건
      break
  return cnt

for _ in range(int(input())):
  N, M = map(int, input().split())
  P = list(map(int, input().split()))
  docs = deque((i, P[i]) for i in range(N))
  print(sol(docs, M))
  