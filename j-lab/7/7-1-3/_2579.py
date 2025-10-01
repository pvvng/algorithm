# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
def sol(n: int, A: list[int]):
	#	dp[i][0] = i번째 계단을 밟았고, 직전 계단은 안 밟음
	#	dp[i][1] = i번째 계단을 밟았고, 직전 계단도 밟음
  dp = [[0] * 2 for _ in range(n)]
  dp[0][0] = A[0]

  for i in range(1, n):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + A[i] # i-2에서 2칸 뛰어와서 i 밟음
    dp[i][1] = dp[i-1][0] + A[i] # i-1 밟았고 그 전 계단은 안 밟음 -> i 밟음
  
  return max(dp[n-1])


n = int(input())
A = [int(input()) for _ in range(n)]
print(sol(n, A))