def sol(n: int, A:list[int]):
  dp = [1] * n # dp[i] = i번째 원소를 끝으로 하는 LIS 길이
  for i in range(n):
    for j in range(i):
      if A[j] < A[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)

n = int(input())
A = list(map(int, input().split()))
print(sol(n, A))