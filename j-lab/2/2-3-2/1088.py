def sol(S:list):
  dct = dict()
  for name in S:
    dct.setdefault(name, 0)
    dct[name] += 1
  return dct

S = input().split()
dct = sol(sorted(S))
for key in dct:
  print(key, dct[key])