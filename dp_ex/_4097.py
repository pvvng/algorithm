import sys
input = sys.stdin.readline

def sol(n: int, p: list):
  # dp[i] = i 구간까지 봤을 때 가장 많은 수익을 올린 구간의 값
  dp = [0] * n
  dp[0] = p[0]

  # 구간 연속 vs. 새 구간 시작
  for i in range(1, n):
    dp[i] = max(dp[i-1] + p[i], p[i])

  return max(dp)

ans = []
while True:
  n = int(input())
  if n == 0:
    break
  p = [int(input()) for _ in range(n)]
  ans.append(str(sol(n, p)))

print("\n".join(ans))