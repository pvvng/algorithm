while True:
  x = int(input())
  if not x:
    break
  cnt = 0 
  for i in range(1, x+1):
    cnt += i
  print(cnt)