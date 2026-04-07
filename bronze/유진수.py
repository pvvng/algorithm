x = input()

if len(x) == 1:
  print("NO")
else:
  ans = False

  for i in range(1, len(x)):
    left = 1
    for c in x[:i]:
      left *= int(c)

    right = 1
    for c in x[i:]:
      right *= int(c)

    if left == right:
      ans = True
      break

  print("YES" if ans else "NO")