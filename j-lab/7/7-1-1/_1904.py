# D[1] = 1, D[2] = 2
# D[n] = D[n-1] + D[n-2]
import sys
input = sys.stdin.readline
MOD = 15746

def sol(n: int):
  if n <= 3:
    return n % MOD
  p, ans = 2, 3
  for _ in range(4, n + 1):
    temp = ans
    # 자릿수 큰 덧셈으로 인한 타임아웃 방지를 위해 모듈러 매 단계마다 적용
    ans = (ans + p) % MOD
    p = temp % MOD
  return ans

print(sol(int(input())))