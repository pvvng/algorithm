def sol(x):
  res = []
  prev = ""
  counter = 1
  for c in x:
    if prev == c:
      counter += 1
    else:
      prev = c
      counter = 1
    res.append(counter)
  return str(max(res))

ans = []
for _ in range(3):
  x = input()
  ans.append(sol(x))
print("\n".join(ans))
