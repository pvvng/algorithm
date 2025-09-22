def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

    

def sol(loc, B):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]

  visited = [[False] * 5 for _ in range(5)]
  visited[loc[0]][loc[1]]
  q = [(loc[0], loc[1], 0)]
  idx = 0

  while idx < len(q):
    crt = q[idx]
    r, c = crt[0], crt[1]
    dist = crt[2]

    if B[r][c] == 1:
      return dist

    idx += 1
    for dr, dc in dt:
      nr, nc = r + dr, c + dc
      if in_range(nr, nc) and not visited[nr][nc] and B[nr][nc] != -1:
        q.append((nr, nc, dist + 1))

    # run
    for dr, dc in dt:
      nr, nc = r, c
      while True:
        if not in_range(nr + dr, nc + dc):
          break
        if B[nr+dr][nc+dc] == -1:
          break
        
        nr += dr; nc += dc
        if B[nr][nc] == 7:
          break
      if not visited[nr][nc]:
        q.append((nr, nc, dist + 1))

  return -1

B = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
print(sol((r, c), B))