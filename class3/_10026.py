import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def in_range(n, r, c):
  return 0 <= r < n and 0 <= c < n

def sol(n, G):
  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  visited = [[False] * n for _ in range(n)]
  visited_RG = [[False] * n for _ in range(n)]

  RG = [("R", "G"), ("G", "R")]

  def dfs(loc, T):
    cr, cc = loc
    for dr, dc in dt:
      nr, nc = cr + dr, cc + dc
      if not in_range(n, nr, nc):
        continue
      cur = G[cr][cc]
      nxt = G[nr][nc]
      # 적록x => 같은 색일 경우만
      if not visited[nr][nc] and T == 0:
        if cur == nxt:
          visited[nr][nc] = True
          dfs((nr, nc), T)
      if not visited_RG[nr][nc] and T == 1:
        if (cur, nxt) in RG or (cur == nxt):
          visited_RG[nr][nc] = True
          dfs((nr, nc), T)

  ret = 0
  ret_RG = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        dfs((i, j), 0)
        ret += 1
      if not visited_RG[i][j]:
        dfs((i, j), 1)
        ret_RG += 1

  return f"{ret} {ret_RG}"

n = int(input())
G = [list(input()) for _ in range(n)]
print(sol(n, G))