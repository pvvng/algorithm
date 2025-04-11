n, m = map(int, input().split())

for i in range (n, m + 1):
  if i < 2:
    continue
  for v in range(2, int(i ** 0.5) + 1):
    if i % v == 0:
      break
  else:
    print(i)