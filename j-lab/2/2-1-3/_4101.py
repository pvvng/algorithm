def sol(x, y):
  if x == 0 and y == 0:
    return 0
  return "Yes" if x > y else "No"

while True:
  x, y = map(int, input().split())
  res = sol(x, y)
  if not res:
    break
  print(res)