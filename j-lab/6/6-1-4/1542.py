def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

def sol(loc, B):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]
  visited = [[[False] * 7 for _ in range(5)] for _ in range(5)]
  # r, c, d, s
  q = [(loc[0], loc[1], 0, 0)]
  visited[loc[0]][loc[1]][0] = True

  idx = 0
  while idx < len(q):  
    r, c, d, s = q[idx]
    idx += 1

    if s == 6:
      return d

    for dr, dc in dt:
      nr = r + dr; nc = c + dc
      if not in_range(nr, nc) or B[nr][nc] == -1:
        continue
      ns = s + 1 if s + 1 == B[nr][nc] else s
      if not visited[nr][nc][ns]:
        q.append((nr, nc, d+1, ns))
        visited[nr][nc][ns] = True

    for dr, dc in dt:
      nr = r; nc = c
      while True:
        if not in_range(nr + dr, nc + dc) or B[nr + dr][nc + dc] == -1:
          break
        nr += dr; nc += dc
        if B[nr][nc] == 7:
          break

      if not in_range(nr, nc) or B[nr][nc] == -1:
        continue
      ns = s + 1 if s + 1 == B[nr][nc] else s
      if not visited[nr][nc][ns]:
        q.append((nr, nc, d+1, ns))
        visited[nr][nc][ns] = True

  return -1

B = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
print(sol((r, c), B))
