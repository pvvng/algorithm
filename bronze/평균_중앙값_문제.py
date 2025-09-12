while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break
  x = sorted([a, b])
  print(2 * x[0] - x[1])
