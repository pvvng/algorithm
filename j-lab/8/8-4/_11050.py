def fac(n):
  res = 1
  for i in range(1, n + 1):
    res *= i
  return res

n, k = map(int, input().split())
print(fac(n) // (fac(k) * fac(n-k)))