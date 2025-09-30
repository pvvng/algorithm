def sol(x: int):
  dp = [0] * (x + 1)
  # 1 -> x 로 가는 최소 연산 횟수
  # 기본전이: +1 -> 직전 값은 i - 1
  # 2의 배수인 경우: *2 -> 직전 값은 i // 2
  # 3의 배수인 경우: *3 -> 직전 값은 i // 3
  for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0 and i // 2 >= 1:
      dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0 and i // 3 >= 1:  
      dp[i] = min(dp[i], dp[i // 3] + 1)
  return dp[x]

x = int(input())
print(sol(x))
