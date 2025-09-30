def in_range(n, i, j):
  return 0 <= j <= i < n 

def sol(n: int, triangle:list[list[int]]):
  dp = [[0] * (i+1) for i in range(n)]
  dp[0][0] = triangle[0][0]
  for i in range(1, n):
    for j in range(i+1):
      prev = 0
      if in_range(n, i-1, j):
        prev = max(dp[i-1][j], prev)
      if in_range(n, i-1, j-1):
        prev = max(dp[i-1][j-1], prev)
      dp[i][j] = prev + triangle[i][j]
  return max(dp[-1])

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, triangle))