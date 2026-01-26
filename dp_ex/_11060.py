# dp[i]
# i번째 칸에 오기까지의 최소 점프거리

# A[i]에 도달하면 dp[i]에서 A[i]만큼의 값을 이동할 수 있다는 뜻이다.
# 따라서 for j in range(i+1, i+A[i]+1) 루프 필수
inf = float("inf")

def sol(n, A):
  dp = [inf] * n
  dp[0] = 0

  for i in range(n):
    for j in range(A[i]):
      if i+j+1 < n:
        dp[i+j+1] = min(dp[i+j+1], dp[i]+1)
  
  return -1 if dp[n-1] == inf else dp[n-1]

n = int(input())
A = list(map(int, input().split()))
print(sol(n, A))