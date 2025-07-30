def sol(n:int, i:int):
  return "*" * (n - i)

n = int(input())
for i in range(n):
  print(sol(n, i))