from collections import deque

def sol(A: list):
  ans = (0, 0)
  d = deque()

  for e in A:
    if e[0] == 2:
      d.popleft()
    elif e[0] == 1:
      d.append(e[1])
    if ans[0] < len(d) or (ans[0] == len(d) and ans[1] > d[0]):
      ans = (len(d), d[0])

  return ans

A = [list(map(int, input().split())) for _ in range(int(input()))]
print(*sol(A))