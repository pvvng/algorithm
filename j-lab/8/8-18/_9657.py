def sol(n):
  if n == 1:
    return True
  if n == 2:
    return False
  if n == 3:
    return True
  if n == 4:
    return True
  
  dp = [False] * (n+1)
  dp[1] = dp[3] = dp[4] = True
  for i in range(5, n+1):
    # 세가지 케이스 중 하나라도 상대가 패배(False)한다면 dp[i] = True
    if not dp[i-4] or not dp[i-3] or not dp[i-1]:
      dp[i] = True
  
  return dp[n]

n = int(input())
print("SK" if sol(n) else "CY")