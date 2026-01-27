import sys
input = sys.stdin.readline

c = min(2, int(float(input()) / 0.99))
n = int(input())
A = list(map(int, input().split()))

# two pointer
def two_pointer(c, n, A):
  left = 0
  right = 0

  mxl = -1
  remain_coins = c
  while right < n:
    if A[right] == 0:
      # 스트릭 프리즈 사용 가능
      if remain_coins > 0:
        remain_coins -= 1
      else:
        remain_coins = c
        left += 1
        right = left
        # 스트릭 파괴
        continue
    mxl = max(mxl, right - left + 1)
    right += 1

  return [mxl, max(A)]

print("\n".join(map(str, two_pointer(c, n, A))))

# dp
def dp(c, n, A):
  dp = [[0] * (c+1) for _ in range(n)]

  dp[0] = [1] * (c+1)

  for i in range(1, n):
    if A[i] > 0:
      for k in range(c+1):
        dp[i][k] = dp[i-1][k] + 1
    else:
      for k in range(1, c+1):
        dp[i][k-1] = dp[i-1][k] + 1

  max_len = -1
  max_sol = max(A)
  for i in range(n):
    for k in range(c+1):
      if dp[i][k] > max_len:
        max_len = dp[i][k]

  return [max_len, max_sol]

print("\n".join(map(str, dp(c, n, A))))
