def sol(n, i):
  return " " * i + "*" * (n - i)

n = int(input())
for i in range(n):
  print(sol(n, i))