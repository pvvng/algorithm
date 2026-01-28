# 배낭 문제
def sol(n, A):
  # 최대 무게가 w인 가방에서 i번째 물건까지 봤을 때 최대 무게
  # dp[w]에서 가지는 최대 무게로 간추릴 수 있다
  dp = [0] * 101

  for j in range(n):
    # 이전 물건을 참조하지 못하도록 역순 루프
    for i in range(100, 0, -1):
      w, v = A[j]
      if i <= w:
        continue
      dp[i] = max(dp[i-w]+v, dp[i])

  return dp[100]

import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
A = []
for i in range(n):
  A.append((L[i], J[i]))
  
print(sol(n, A))