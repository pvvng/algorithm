n, k = map(int, input().split())
L = list(map(int, input().split()))

dp = [[1] * 2 for _ in range(n)]

for i in range(n-1):
  # 점프를 한다
  if L[i] > k:
    dp[i][0] = dp[i-1][1] + 1
    dp[i][1] = 1
  # 점프를 하지 않는다
  else:
    dp[i][0] = dp[i-1][0] + 1 
    dp[i][1] = dp[i-1][1] + 1 

ans = max(list(map(lambda x: max(x), dp[:n-1])))
print(ans)
