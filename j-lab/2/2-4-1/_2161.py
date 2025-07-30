from collections import deque

def sol(N: int):
  deq = deque()
  ans = []
  for i in range(1, N +1):
    deq.append(i)
  while len(deq) > 1:
    ans.append(deq.popleft())
    deq.append(deq.popleft())
  ans.append(deq.popleft())

  return ans

print(*sol(int(input())))