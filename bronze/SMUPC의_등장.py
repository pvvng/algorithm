x = input()
for i in range(len(x)):
  t = list(str(ord(x[i])))
  s = sum(list(map(int, t)))
  print(x[i] * s)
