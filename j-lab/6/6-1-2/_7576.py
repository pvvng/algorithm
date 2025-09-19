# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
def in_range(r, c, n, m):
  return 0 <= r < n and 0 <= c < m

def sol(n:int, m:int, T:list[list[int]]):
  queue = []
  visited = [[False] * m for _ in range(n)]

  for r in range(n):
    for c in range(m):
      if T[r][c] == 1:
        queue.append((r, c, 0))
        visited[r][c] = True
      if T[r][c] == -1:
        visited[r][c] = True

  if len(queue) == 0:
    return -1

  idx = 0
  dt = [(0,1),(0,-1),(1,0),(-1,0)]
  while idx < len(queue):
    crt = queue[idx]
    idx += 1
    for d in dt:
      nr, nc = crt[0] + d[0], crt[1] + d[1]
      day = crt[2]
      if not in_range(nr, nc, n, m):
        continue
      if visited[nr][nc]:
        continue
      queue.append((nr, nc, day + 1))
      visited[nr][nc] = True

  for r in range(n):
    for c in range(m):
      if not visited[r][c]:
        return -1

  return queue[-1][2]

m, n = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, m, T))
