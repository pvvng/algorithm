# 재귀 피보나치의 실행 횟수는 피보나치 값과 같다
# dp 피보나치 실행 횟수는 반복문 시행 횟수와 같다. 즉 n - 2.
def fib(n : int):
  dp = [0] * (n + 1)
  dp[1] = dp[2] = 1
  for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

n = int(input())
print(fib(n), n - 2)