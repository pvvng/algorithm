def fac(n: int):
  dp = [1] * (n+1)
  for i in range(1, n + 1):
    dp[i] = dp[i-1] * i
  return dp[n]

def sol(T):
  ans = []
  for t in T:
    ans.append(str(fac(t))[-1])
  return "\n".join(ans)

print(sol([int(input()) for _ in range(int(input()))]))