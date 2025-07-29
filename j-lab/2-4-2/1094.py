from collections import deque

def transform(target: list):
  if len(target) == 0:
    return "None"
  return " ".join(map(str, sorted(target)))

def sol(S: list):
  deq = deque()
  A, B, C = [], [], []
  for s in S:
    if s[0] == 2:
      p = deq.popleft()
      if p[1] == s[1]:
        A.append(p[0])
      else:
        B.append(p[0])
    elif s[0] == 1:
      deq.append((s[1], s[2]))
  for d in deq:
    C.append(d[0])

  return (A, B, C)

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
(A, B, C) = sol(S)
print(transform(A))
print(transform(B))
print(transform(C))