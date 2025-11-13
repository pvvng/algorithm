def sol(n):
  if n == 1:
    return False
  if n == 2:
    return True
  if n == 3:
    return False
  
  # dp[i]
  dp = [False] * (n+1)
  dp[2] = True
  for i in range(4, n + 1):
    # i 상태에서 돌을 1개 혹은 3개 가져갔을 때 상태에서 상대가 패배하면 나는 승리임
    if not dp[i-1] or not dp[i-3]:
      dp[i] = True
  
  return dp[n]

n = int(input())
print("SK" if sol(n) else "CY")
