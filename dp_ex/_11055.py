def sol(n, A):
  # dp[i]
  # i를 마지막 요소로 가지는 부분 수열의 최대합
  dp = A.copy()
  
  for i in range(1, n):
    for j in range(i):
      # 부분 수열이 가능한 값을 확인한다.
      if A[i] > A[j]:
        dp[i] = max(dp[i], dp[j] + A[i]) # 최댓값을 저장한다.
  
  return max(dp)

n = int(input())
A = list(map(int, input().split()))
print(sol(n, A))
