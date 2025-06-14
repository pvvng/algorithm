mx = -1
cu = ""
for _ in range(7):
  x, y = input().split()
  y = int(y)
  if y >= mx:
    cu = x
    mx = y
print(cu)
