import sys
input = sys.stdin.readline

def sol(R, C, B):
  # 한 지점 시작점으로 두고 우, 하 루프를 돌린다.
  # visited[t][r] bottom일때 방문, right일때 방문했는지 체크
  visited = [[[False] * 2 for _ in range(C)] for _ in range(R)]

  def in_range(r, c):
    return 0 <= r < R and 0 <= c < C

  def dfs(goto, cur):
    r, c = cur
    ret = B[r][c]

    if goto == "right":
      nr, nc = r, c + 1
      if in_range(nr, nc) and not visited[nr][nc][0] and B[nr][nc] != "#":
        visited[nr][nc][0] = True
        ret += dfs(goto, (nr, nc))

    if goto == "bottom":
      nr, nc = r + 1, c
      if in_range(nr, nc) and not visited[nr][nc][1] and B[nr][nc] != "#":
        visited[nr][nc][1] = True
        ret += dfs(goto, (nr, nc))

    return ret

  cands = []
  for i in range(R):
    for j in range(C):
      if B[i][j] == "#":
        continue
      if not visited[i][j][0]:
        visited[i][j][0] = True
        ret = dfs("right", (i, j))
        if len(ret) > 1:
          cands.append(ret)
      if not visited[i][j][1]:
        visited[i][j][1] = True
        ret = dfs("bottom", (i, j))
        if len(ret) > 1:
          cands.append(ret)

  cands.sort()
  return cands[0]

n, m = map(int, input().split())
B = [list(input()) for _ in range(n)]  
print(sol(n, m, B))