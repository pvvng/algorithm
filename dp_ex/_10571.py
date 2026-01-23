#  중량이 높아지고, 선명도 값이 낮아지는 부분열 중 최장의 것의 길이
def sol(n: int, D: list):
  # dp[i] => i가 부분열의 마지막 요소일 때 부분열의 최대 길이
  dp = [0] * n
  dp[0] = 1

  for i in range(1, n):
    cw, cc = D[i] # 현재 중량, 현재 선명도
    max_len = 0
    for j in range(i): # 이전 값 중 연결 가능한 값을 찾는다.
      pw, pc = D[j]
      if pw >= cw or pc <= cc: # 연결 불가능
        continue
      max_len = max(max_len, dp[j]) # 연결 가능한 값 중 최댓값을 연결한다.
    dp[i] = max_len + 1
      
  return max(dp)

import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
  n = int(input())
  D = [tuple(map(float, input().split())) for _ in range(n)]
  ans.append(sol(n, D))
print("\n".join(map(str, ans)))