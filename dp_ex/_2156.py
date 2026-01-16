# 연속으로 세잔은 못마신다.
# dp[i][k]:
# i 현재 인덱스 (잔)
# k 이번 잔을 포함해서 이전까지 연속으로 마신 술의 개수
# k = 0, 이번 잔을 마시지 않았다. 
# k = 1, 이번 잔을 마셨다.
# k = 2, 이번 잔을 마셨고, 그 이전 잔도 마셨다. (다음 잔에서 못마신다.)

# dp[i]:
# 이전 누적합중 최댓값
# dp[i][0] = max(dp[i-1])
# 이전에 마시지 않을 경우 + 현재값
# dp[i][1] = dp[i-1][0] + items[i]
# 이전에 마신 경우 + 현재값
# dp[i][2] = dp[i-1][1] + items[i]

import sys
input = sys.stdin.readline

n = int(input())
items = [int(input()) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = 0
dp[0][1] = items[0]
dp[0][2] = items[0]

for i in range(1, n):
  dp[i][0] = max(dp[i-1])
  dp[i][1] = dp[i-1][0] + items[i]
  dp[i][2] = dp[i-1][1] + items[i]

print(max(dp[n-1]))