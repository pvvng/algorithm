def sol(x, y):
  if x == y:
    return "=="
  elif x > y:
    return ">"
  else:
    return "<"

x, y = map(int, input().split())
print(sol(x, y))