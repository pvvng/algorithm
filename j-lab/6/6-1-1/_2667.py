def in_range(r, c, n):
  return 0 <= r <= n - 1 and 0 <= c <= n - 1

def bfs(n:int, APT, queue: list[tuple[int, int]], visited: set):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]

  idx = 0
  count = 0
  while idx < len(queue):
    crt = queue[idx]
    idx += 1
    count += 1

    for d in dt:
      nr, nc = crt[0] + d[0], crt[1] + d[1]
      if in_range(nr, nc, n) and (nr, nc) not in visited and APT[nr][nc] == "1":
        queue.append((nr, nc))
        visited.add((nr, nc))

  return count

def sol(n, APT):
  visited = set()
  ans = []
  for i in range(n):
    for j in range(n):
      if APT[i][j] == "1" and (i, j) not in visited:
        visited.add((i, j))
        ans.append(bfs(n, APT, [(i, j)], visited))
        
  return sorted(ans)

n = int(input())
APT = [list(input()) for _ in range(n)]
ans = sol(n, APT)
print(len(ans))
for e in ans:
  print(e)