def sol(n):
  if n == 1:
    return True
  if n == 2:
    return False
  if n == 3:
    return True
  
  # dp[i]: 현재 사람이 i개의 돌이 있는 상태에서 이긴다.
  dp = [False] * (n+1)
  dp[1] = True # i가 1일 경우엔 필승
  dp[2] = False # i가 2일 경우엔 필패
  dp[3] = True # i가 3일 경우엔 필승
  for i in range(4, n+1):
    # 현재(i) 상태에서 
    # 돌을 1개 빼서(dp[i-1]) 상대가 지면(dp[i-1] = False) dp[i] = True
    # 돌을 3개 빼서(dp[i-3]) 상대가 지면(dp[i-1] = False) dp[i] = True
    if not dp[i-1] or not dp[i-3]:
      dp[i] = True
  
  return dp[n]

n = int(input())
print("SK" if sol(n) else "CY")