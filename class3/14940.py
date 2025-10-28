def in_range(cur, n, m):
  return 0 <= cur[0] < n and 0 <= cur[1] < m

def sol(n, m, mp):
  dist = [["-1"] * m for _ in range(n)]
  visited = [[False] * m for _ in range(n)]
  dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  start = None
  for i in range(n):
    for j in range(m):
      if mp[i][j] == 2:
        start = (i, j, 0)
        dist[i][j] = str(0)
      if mp[i][j] == 0:
        dist[i][j] = str(0)
  
  q = [start]
  visited[start[0]][start[1]] = True
  idx = 0
  while idx < len(q):
    cn, cm, cur_move = q[idx]
    idx += 1
    for dn, dm in dd:
      nn, nm = cn + dn, cm + dm
      if not in_range((nn, nm), n, m):
        continue
      if visited[nn][nm]:
        continue
      visited[nn][nm] = True

      if mp[nn][nm] != 0:
        dist[nn][nm] = str(cur_move + 1)
        q.append((nn, nm, cur_move + 1))
      else:
        dist[nn][nm] = str(0)

  return dist

# n은 세로의 크기, m은 가로의 크기다
n, m = map(int, input().split())
mp = []
for _ in range(n):
  mp.append(list(map(int, input().split())))
ans = sol(n, m, mp)
ans = list(map(lambda x : " ".join(x), ans))
print("\n".join(ans))
