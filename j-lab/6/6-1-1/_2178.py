def in_range(n, m, r, c):
  return 0 <= r <= n - 1 and 0 <= c <= m - 1

def sol(n:int, m:int, miro:list[list[int]], queue: list[tuple[int, int]], visited:set):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]

  idx = 0
  while idx < len(queue):
    crt = queue[idx]
    idx += 1

    if crt[0] == n - 1 and crt[1] == m - 1:
      return crt[2]

    for d in dt:
      nr, nc = crt[0] + d[0], crt[1] + d[1]
      dist = crt[2]
      if in_range(n, m, nr, nc) and (nr, nc) not in visited and miro[nr][nc] == "1":
        visited.add((nr, nc))
        queue.append((nr, nc, dist + 1))

n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]
print(sol(n, m, miro, [(0,0,1)], set()))