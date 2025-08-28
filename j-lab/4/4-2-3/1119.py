def F(n: int):
  if n == 1 or n == 2:
    return 1
  return F(n - 1) + F(n - 2)

print(F(int(input())))