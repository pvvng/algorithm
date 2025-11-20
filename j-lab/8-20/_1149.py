# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 모든 집을 칠하는 비용의 최솟값
import sys
input = sys.stdin.readline

def sol(n, weight):
  # R -> 0, G -> 1, B -> 2
  dp = [None]
  for _ in range(n):
    dp.append([0, 0, 0])
  # init
  dp[1][0] = weight[1][0]
  dp[1][1] = weight[1][1]
  dp[1][2] = weight[1][2]

  # i를 R로 선택했다면 i-1은 G, B중 최솟값이 되어야 함
  # dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + weight[i][R]
  for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + weight[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + weight[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + weight[i][2]
  
  return min(dp[n][0], dp[n][1], dp[n][2])

n = int(input())
weight = [None]
for _ in range(n):
  weight.append(list(map(int, input().split())))

print(sol(n, weight))