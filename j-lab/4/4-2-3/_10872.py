def fac(n: int):
  if n <= 1:
    return 1
  return n * fac(n - 1)

def sol(n: int):
  d = 1
  if n == 0:
    return 1
  for i in range(1, n+1):
    d *= i
  return d

n = int(input())
print(fac(n))
print(sol(n))
