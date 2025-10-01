MOD = 1000000000

def sol(n: int):
  prev = [0] * 10
  for d in range(1, 10):
    prev[d] = 1

  for _ in range(n-1):
    cur = [0] * 10
    for j in range(10):
      if j > 0:
        cur[j] = (cur[j] + prev[j-1]) % MOD
      if j < 9:
        cur[j] = (cur[j] + prev[j+1]) % MOD
    prev = cur

  return sum(prev) % MOD

n = int(input())
print(sol(n))
