import sys
input = sys.stdin.readline

# (0,0) -> (n-1,m-1)
def sol(n, m, A):
  # dp[r][c] 
  # (r, c)에 도달했을때 얻을 수 있는 사탕의 최댓값
  # (-1, 0), (0, -1), (-1, -1) 중 가장 사탕을 많이 가지고 있는 값에 현잿값을 더한다.

  # init dp list
  dp = [[0] * m for _ in range(n)]
  dp[0][0] = A[0][0]
  for r in range(1, n):
    dp[r][0] = dp[r-1][0] + A[r][0]
  for c in range(1, m):
    dp[0][c] = dp[0][c-1] + A[0][c]
  
  # 1초
  for r in range(1, n):
    for c in range(1, m):
      dp[r][c] = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + A[r][c]

  return dp[n-1][m-1]

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, m, A))
