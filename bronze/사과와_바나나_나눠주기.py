def sol(r, a, b):
  for i in range(1, r):
    if a % i == 0 and b % i == 0:
      print(i, a // i, b // i)

a, b = map(int, input().split())
if a > b:
  sol(b + 1, a, b)
else:
  sol(a + 1, a, b)
