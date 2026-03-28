n, m, a, b = map(int, input().split())
if m >= n * 3:
  print(0)
else:
  print((n * 3 - m) * a + b)