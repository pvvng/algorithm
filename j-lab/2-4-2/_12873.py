from collections import deque

def sol(N:int) -> int:
  d = deque()
  for i in range(1, N + 1):
    d.append(i)
  step = 1
  while len(d) > 1:
    rotate = ((step ** 3) % len(d)) - 1
    d.rotate(-rotate)
    d.popleft()
    step += 1
  return d[0]

N = int(input())
print(sol(N))