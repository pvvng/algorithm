import sys
input = sys.stdin.readline

# 특정 지점에 도달할 때 이전 상태에 따라서 이 지점을 사용할지 말지를 정한다
# 이러한 문제는 특정 지점을 여러번 방문할 수 있으므로 visited 배열이 필요하지 않다.
# 핵심은 특정 지점에 방문했을때의 상태를 저장하여 비교하는 것이다.
def sol(r, c, B):
  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  # 특정 지점 (r, c)에 도착했을때의 Path를 기록한다.
  q = set([(0, 0, B[0][0])])
  ans = 0
  while q:
    cr, cc, path = q.pop()
    ans = max(ans, len(path))
    for dr, dc in dt:
      nr, nc = cr + dr, cc + dc
      if 0 <= nr < r and 0 <= nc < c and B[nr][nc] not in path:
        q.add((nr, nc, path + B[nr][nc]))
  return ans
  
r, c = map(int, input().split())
B = [list(input().strip()) for _ in range(r)]
print(sol(r, c, B))
