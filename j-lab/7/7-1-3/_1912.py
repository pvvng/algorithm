# dp[i] 는 i를 마지막 원소로 반드시 포함하는 수열의 최댓값
def sol(n: int, A: list[int]):
  dp = [0] * n
  dp[0] = A[0]
  for i in range(1, n):
    if dp[i - 1] < 0:
      dp[i] = A[i]
    else:
      dp[i] += dp[i-1] + A[i]
  return max(dp)

n = int(input())
A = list(map(int, input().split()))
print(sol(n, A))
