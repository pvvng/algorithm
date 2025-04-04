co = []

while(True):
  n = input()
  if(n == "0"): break
  m = len(n)
  isDrom = True
  for i in range(m):
    z =  m - i - 1
    if(i > z): 
      break
    if(n[i] != n[z]): 
      isDrom = False
  if(isDrom): 
    co.append("yes")
  else:
    co.append("no")

for v in co:
  print(v)