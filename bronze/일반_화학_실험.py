idx = -1
prev = 0
while True:
  temp = float(input())
  if temp == 999:
    break
  if idx == -1:
    prev = temp
  else:
    print("{:.2f}".format(temp - prev))
    prev = temp
  idx += 1  