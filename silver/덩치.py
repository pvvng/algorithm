n = int(input())

dcs = []

for _ in range(n):
  x, y = map(int, input().split())
  dcs.append((x, y))

ans = []

for i in range(len(dcs)):
  lg = 1
  (x, y) = dcs[i]
  for j in range(0, len(dcs)):
    if i == j:
      continue
    (p, q) = dcs[j]
    if x < p and y < q:
      lg += 1
  ans.append(lg)

for v in ans:
  print(v)