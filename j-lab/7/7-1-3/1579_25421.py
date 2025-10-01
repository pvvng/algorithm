def sol(n: int):
  # dp[i][j] -> 자릿수가 i일 경우 마지막 자릿수가 j일때 가능한 경우의 수 모음
  dp = [[0] * 10 for _ in range(n+1)]
  for j in range(1, 10):
    dp[1][j] = 1
  
  for i in range(2, n + 1):
    for j in range(1, 10):
      # 현재 자릿수가 i이고 마지막 숫자가 j일때 직전 자릿수 (i-1)에서 가능한 자릿수 모두 더하기
      s = max(1, j - 2)
      e = min(9, j + 2)
      for k in range(s, e+1):
        dp[i][j] += dp[i-1][k]
      dp[i][j] %= 987654321

  return sum(dp[n]) % 987654321

n = int(input())
print(sol(n))