# f(n)의 모든 경우의 수는 다음과 같다.
# (...) + 1 -> n => (...) -> n - 1: 마지막에 +1을 더하는 경우
# (...) + 2 -> n => (...) -> n - 2 : 마지막에 +2을 더하는 경우
# (...) + 3 -> n => (...) -> n - 3 : 마지막에 +3을 더하는 경우
# 즉, f(n) = f(n-1) + f(n-2) +f(n-3)

import sys
input = sys.stdin.readline

f = [None] * 12
f[1] = 1; f[2] = 2; f[3] = 4

def sol(n):
  if f[n] != None:
    return f[n]
  
  for i in range(4, n + 1):
    f[i] = f[i-1] + f[i-2] + f[i-3]
  
  return f[i]

ans = []
for _ in range(int(input())):
  ret = sol(int(input()))
  ans.append(str(ret))
print("\n".join(ans))