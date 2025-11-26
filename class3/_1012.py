import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# r = n, c = m
def sol(n, m, B):
  ret = 0
  visited = [[True] * m for _ in range(n)]

  for bc, br in B:
    visited[br][bc] = False

  for bc, br in B:
    if not visited[br][bc]:
      dfs(br, bc, visited, n, m)
      ret += 1

  return str(ret)

def in_range(r, c, n, m):
  return 0 <= r < n and 0 <= c < m

def dfs(r, c, visited, n, m):
  visited[r][c] = True

  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for dr, dc in dt:
    nr, nc = dr + r, dc + c
    if in_range(nr, nc, n, m) and not visited[nr][nc]:
      dfs(nr, nc, visited, n, m)

ans = []
for _ in range(int(input())):
  m, n, k = map(int, input().split())
  # 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
  B = [tuple(map(int, input().split())) for _ in range(k)]
  ans.append(sol(n, m, B))
print("\n".join(ans))