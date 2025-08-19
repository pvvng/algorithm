def sqrt(num):
  return num ** 0.5

cnt = 0

while True:
  a, b, c = map(int, input().split())
  if a + b + c == 0:
    break

  cnt += 1

  print(f"Triangle #{cnt}")
  if a == -1:
    x = c ** 2 - b ** 2
    if x > 0:
      print("a = {:.3f}".format(sqrt(x)))
    else:
      print("Impossible.")
  if b == -1:
    x = c ** 2 - a ** 2
    if x > 0:
      print("b = {:.3f}".format(sqrt(x)))
    else:
      print("Impossible.")
  if c== -1:
    x = a ** 2 + b ** 2
    if x > 0:
      print("c = {:.3f}".format(sqrt(x)))
    else:
      print("Impossible.")

  print()