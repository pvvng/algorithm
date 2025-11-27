import sys
input = sys.stdin.readline

def find(n, m, C):
  for i in range(n):
    for j in range(m):
      if C[i][j] == "I":
        return (i, j)
      
def in_range(n, m, r, c):
  return 0 <= r < n and 0 <= c < m

def sol(n, m, C):
  visited = [[False] * m for _ in range(n)]

  ir, ic = find(n, m, C)
  visited[ir][ic] = True

  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
  ans = 0
  q = [(ir, ic)]
  idx = 0  
  while idx < len(q):
    r, c = q[idx]
    idx += 1
    for dr, dc in dt:
      nr, nc = r + dr, c + dc
      if in_range(n, m, nr, nc) and not visited[nr][nc] and C[nr][nc] != "X":
        if C[nr][nc] == "P":
          ans += 1
        visited[nr][nc] = True
        q.append((nr, nc))

  return "TT" if ans == 0 else str(ans)

# n = r, m = c
n, m = map(int, input().split())
C = [list(input()) for _ in range(n)]
print(sol(n, m, C))