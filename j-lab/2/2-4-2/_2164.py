from collections import deque

def sol(N:int) -> int:
  deq = deque()
  for i in range(1, N + 1):
    deq.append(i)
  while len(deq) > 1:
    deq.popleft()
    p = deq.popleft()
    deq.append(p)
  return deq[0]

N = int(input())
print(sol(N))
