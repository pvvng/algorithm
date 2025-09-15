def sol(a, b, c):
  d = {}
  for i in range(10):
    d.setdefault(str(i), 0)
  t = a * b * c
  ls = list(str(t))
  for e in ls:
    d[e] += 1
  return d
  
a = int(input())
b = int(input())
c = int(input())
d = sol(a, b, c)
for key in d:
  print(d[key])