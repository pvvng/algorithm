
while True:
  ls = list(map(int, input().split()))

  target = ls[0]
  if target == 0:
    break

  ans = []
  prev = -1
  for i in range(1, target + 1):
    crt = ls[i]
    if prev != crt:
      ans.append(crt)
    prev = crt

  for e in ans:
    print(e, end=" ")
  print("$")