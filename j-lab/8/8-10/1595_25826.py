import sys
input = sys.stdin.readline

def sol(n, A, dp, rt: tuple[int, int], ct: tuple[int, int]):
  # 행의 누적합 계산
  for r in range(n):
    for c in range(1, n):
      dp[r][c] += dp[r][c-1]

  # 열의 누적합 계산
  for c in range(n):
    for r in range(1, n):
      dp[r][c] += dp[r-1][c]

  ans = 0
  for r in range(rt[0], rt[1] + 1): 
    for c in range(ct[0], ct[1] + 1):
      ans += A[r][c] + dp[r][c]

  return ans

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
r1, r2, c1, c2 = 0, 0, 0, 0
for _ in range(m): # 스트리밍
  q, i1, j1, i2, j2, *rest = tuple(map(int, input().split()))
  if q == 1:
    k = rest[0]
    dp[i1][j1] += k
    if j2 + 1 < n:
      dp[i1][j2 + 1] -= k
    if i2 + 1 < n:
      dp[i2 + 1][j1] -= k
    if i2 + 1 < n and j2 + 1 < n:
      dp[i2 + 1][j2 + 1] += k
    
  else:
    c1, c2 = j1, j2 
    r1, r2 = i1, i2
  
print(sol(n, A, dp, (r1, r2), (c1, c2)))