import sys
input = sys.stdin.readline
from collections import deque

# def D(n): 
#   return (n * 2) % 10000

# def S(n): 
#   return 9999 if n == 0 else n - 1

# def L(n):
#   return (n % 1000) * 10 + n // 1000

# def R(n):
#   return (n % 10) * 1000 + n // 10

def sol(a, b):
  if a == b:
    return ""
  
  deq = deque()
  deq.append(a)

  visited = [False] * 10000
  visited[a] = True

  from_where = [-1] * 10000
  how = [""] * 10000

  while deq:
    cur = deq.popleft()

    if cur == b:
      break

    nxt = (cur * 2) % 10000
    if not visited[nxt]:
      visited[nxt] = True
      from_where[nxt] = cur
      how[nxt] = 'D'
      if nxt == b:
        break
      deq.append(nxt)

    nxt = 9999 if cur == 0 else cur - 1
    if not visited[nxt]:
      visited[nxt] = True
      from_where[nxt] = cur
      how[nxt] = 'S'
      if nxt == b:
        break
      deq.append(nxt)

    nxt = (cur % 1000) * 10 + cur // 1000
    if not visited[nxt]:
      visited[nxt] = True
      from_where[nxt] = cur
      how[nxt] = 'L'
      if nxt == b:
        break
      deq.append(nxt)

    nxt = (cur % 10) * 1000 + cur // 10
    if not visited[nxt]:
      visited[nxt] = True
      from_where[nxt] = cur
      how[nxt] = 'R'
      if nxt == b:
        break
      deq.append(nxt)
    
  # 역추적
  res = []
  cur = b
  while cur != a:
    res.append(how[cur])
    cur = from_where[cur]
  
  return "".join(reversed(res))

ans = []
T = int(input())
for _ in range(T):
  a, b = tuple(map(int, input().split()))
  ans.append(sol(a, b))
print("\n".join(ans))