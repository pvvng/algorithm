def sol(R, C, B):
  def in_range(nr, nc):
    return 0 <= nr < R and 0 <= nc < C

  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  def dfs(r, c, visited):
    ret = 1
    for dr, dc in dt:
      nr, nc = r + dr, c + dc
      if in_range(nr, nc) and not visited[nr][nc] and B[nr][nc] == B[r][c]:
        visited[nr][nc] = True
        ret += dfs(nr, nc, visited)
    
    return ret

  white = []
  blue = []
  for i in range(R):
    for j in range(C):
      if B[i][j] == "B":
        blue.append((i, j))
      else:
        white.append((i, j))

  def exec(target):
    visited = [[False] * C for _ in range(R)]
    ans = 0
    for ti, tj in target:
      if not visited[ti][tj]:
        visited[ti][tj] = True
        ret = dfs(ti, tj, visited)
        ans += ret ** 2
    return ans

  return [exec(white), exec(blue)]


import sys
input = sys.stdin.readline

c, r = map(int, input().split())
B = [input() for _ in range(r)]  

print(" ".join(map(str, sol(r, c, B))))