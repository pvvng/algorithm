r = []
while(True):
  ls = list(map(int, input().split()))
  if(ls[0] == 0 and ls[1] == 0 and ls[2] == 0): break
  high = max(ls)
  ls = list(filter(lambda x : x != high, ls))
  high = high ** 2
  sum = 0
  for v in ls:
    sum += v**2
  if(high == sum):
    r.append("right")
  else:
    r.append("wrong")
  
for v in r:
  print(v)