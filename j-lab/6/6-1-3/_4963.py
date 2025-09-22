def in_range(r, c, nr, nc):
  return 0 <= nr < r and 0 <= nc < c

def sol(r, c, I):
  dt = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
  visited = [[False] * c for _ in range(r)]

  res = 0
  for i in range(r):
    for j in range(c):
      if I[i][j] != 1 or visited[i][j]:
        continue

      res += 1
      q = [(i, j)]
      visited[i][j] = True
      idx = 0
      while idx < len(q):
        cr, cc = q[idx]
        idx += 1
        for dr, dc in dt:
          nr = cr + dr; nc = cc + dc
          if in_range(r, c, nr, nc) and not visited[nr][nc] and I[nr][nc] == 1:
            q.append((nr, nc))
            visited[nr][nc] = True
    
  return str(res)

ans = []
while True:
  c, r = map(int, input().split())
  if r + c == 0:
    break
  I = [list(map(int, input().split())) for _ in range(r)]
  ans.append(sol(r, c, I))

print("\n".join(ans))