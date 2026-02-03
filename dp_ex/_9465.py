import sys
input = sys.stdin.readline

# n-2 이하 모든 요소 중 최댓값을 선택하거나
# n-1 대각 요소를 선택하기
def sol(n, A):
  # r = 2, c = n
  dp = [[0] * n for _ in range(2)]
  dp[0][0] = A[0][0]
  dp[1][0] = A[1][0]

  mx = max(A[0][0], A[1][0])

  for i in range(1, n):
    # 1. 직전 값과 대각연결
    dp[0][i] = dp[1][i-1] + A[0][i]
    dp[1][i] = dp[0][i-1] + A[1][i]

    # 2. n-2 이하 값중 최대와 이을지
    if i > 1:
      if dp[0][i] < mx + A[0][i]:
        dp[0][i] = mx + A[0][i]
      if dp[1][i] < mx + A[1][i]:
        dp[1][i] = mx + A[1][i]
      # 3. 최댓값 갱신
      mx = max(mx, dp[0][i-1], dp[1][i-1])

  return max(max(dp[0]), max(dp[1]))

ans = []
for _ in range(int(input())):
  n = int(input())
  A = [list(map(int, input().split())) for _ in range(2)]
  ans.append(sol(n, A))

print("\n".join(map(str, ans)))
    