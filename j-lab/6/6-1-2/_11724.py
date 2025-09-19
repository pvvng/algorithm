import sys
input = sys.stdin.readline

def sol(T: list, n: int):
  nodes = [[] for _ in range(n)]
  for a, b in T:
    nodes[a - 1].append(b - 1)
    nodes[b - 1].append(a - 1)

  visited = [False] * n
  ans = 0
  for i in range(n):
    if visited[i]:
      continue
    q = [i] # i가 시작점
    idx = 0
    visited[i] = True
    while idx < len(q):
      for nxt in nodes[q[idx]]:
        if not visited[nxt]:
          q.append(nxt)
          visited[nxt] = True
      idx += 1
    ans += 1
  return ans

n, m = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(m)]
print(sol(T, n))