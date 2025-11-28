import sys
input = sys.stdin.readline

# M은 상자의 가로 칸의 수(c), N은 상자의 세로 칸의 수 (r)
# 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보
# 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보
# 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다
# N개의 줄이 H번 반복하여 주어진다
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# B[h][r][c]

def in_range(r, c, ht, n, m, h):
  def range_check(a, b):
    return 0 <= a < b
  return range_check(r, n) and range_check(c, m) and range_check(ht, h)

def sol(m, n, h, B):
  totals = m * n * h

  visited = [[[False] * m for _ in range(n)] for _ in range(h)]

  q = []
  for ht in range(h):
    for rt in range(n):
      for ct in range(m):
        if B[ht][rt][ct] == 1:
          q.append((rt, ct, ht, 0))
          visited[ht][rt][ct] = True
        elif B[ht][rt][ct] == -1:
          totals -= 1
          visited[ht][rt][ct] = True

  # 토마토가 모두 익은 상태로 시작했을 경우 종료
  if len(q) == totals:
    return 0

  # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
  dt = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)] 

  idx = 0
  while idx < len(q):
    cr, cc, ch, day = q[idx]
    idx += 1

    if len(q) == totals:
      return q[-1][3]

    for dr, dc, dh in dt:
      nr, nc, nh = cr + dr, cc + dc, ch + dh
      if in_range(nr, nc, nh, n, m, h) and not visited[nh][nr][nc]:
        visited[nh][nr][nc] = True
        q.append((nr, nc, nh, day + 1))
    
  return -1

m, n, h = map(int, input().split())

B = []
for _ in range(h):
  B.append([list(map(int, input().split())) for _ in range(n)])

print(sol(m, n, h, B))