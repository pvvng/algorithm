import sys
input = sys.stdin.readline

def in_range(n, m, r, c):
  return 0 <= r < n and 0 <= c < m

def sol(n, m, b, maxy):
  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  visited = [[False] * m for _ in range(n)]

  ans = 0

  def dfs(loc, cnt, score):
    nonlocal ans, maxy

    # 가지치기
    if score + (4 - cnt) * maxy <= ans:
      return 0

    if cnt == 4:
      return score
    
    cr, cc = loc
    ret = 0
    for dr, dc in dt:
      nr, nc = cr + dr, cc + dc
      if in_range(n, m, nr, nc) and not visited[nr][nc]:
        visited[nr][nc] = True
        ret = max(ret, dfs((nr, nc), cnt + 1, score + b[nr][nc]))
        visited[nr][nc] = False

    return ret

  # ㅗ 추가 검증
  def check_t(r, c):
    avs = [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]
    cds = []
    for nr, nc in avs:
      if not in_range(n, m, nr, nc):
        continue
      cds.append(b[nr][nc])
    if len(cds) < 3:
      return 0
    return b[r][c] + sum(cds) - (0 if len(cds) == 3 else min(cds))

  for r in range(n):
    for c in range(m):
      ans = max(ans, check_t(r, c), dfs((r, c), 0, 0))

  return ans

n, m = map(int, input().split())
b = []
maxy = -1
for _ in range(n):
  col = list(map(int, input().split()))
  b.append(col)
  maxy = max(maxy, max(col))

print(sol(n, m, b, maxy))