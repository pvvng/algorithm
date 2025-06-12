sleep = int(input())
wake = int(input())

if 0 <= sleep <= 3:
  print(wake - sleep)
else :
  print(24 - sleep + wake)