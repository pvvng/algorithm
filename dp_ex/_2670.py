# dp[i]
# i 이전의 최적해를 사용하는 것이 좋은지, 안좋은지를 판별해서 저장한다.
# 좋은 경우(커지는 경우)에는 dp[i] = dp[i-1]*items[i]
# 안좋은 경우(작아지는 경우)에는 dp[i] = items[i]
# 좋은 경우/안좋은 경우 분류:
# dp[i-1] * items[i] > items[i]
import sys
input = sys.stdin.readline

n = int(input())
items = [float(input()) for _ in range(n)]

dp = [0.0] * n
dp[0] = items[0]

for i in range(1, n):
  dp[i] = max(dp[i-1]*items[i], items[i])

print(f"{max(dp):.3f}")