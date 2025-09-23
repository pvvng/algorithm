def in_range(n, m, r, c):
  return 0 <= r < n and 0 <= c < m

def sol(n: int, m: int, A:list[list[int]]):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]
  visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
  visited[0][0][0] = True

  idx = 0
  # r, c, dist, wall (T/F -> 1/0)
  q = [(0, 0, 1, 0)]
  while idx < len(q):
    r, c, dist, wall = q[idx]

    if r == n - 1 and c == m - 1:
      return dist

    idx += 1
    for dr, dc in dt:
      nr = r + dr; nc = c + dc
      nw = wall
      if not in_range(n, m, nr, nc):
        continue  
      if A[nr][nc] == 1: 
        if wall == 1: # 이미 벽을 부순 상태
          continue
        else:
          nw = 1
      if not visited[nr][nc][nw]:
        q.append((nr, nc, dist + 1, nw))
        visited[nr][nc][nw] = True

  return -1

n, m = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(n)]
print(sol(n, m, A))