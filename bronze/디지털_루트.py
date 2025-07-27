while True:
  x = input()
  if x == "0":
    break
  while len(x) > 1:
    ls = list(map(int, list(x)))
    x = str(sum(ls))
  print(x)
