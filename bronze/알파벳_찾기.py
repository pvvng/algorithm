dc = {}
for i in range(26):
  dc[chr(i + 97)] = -1

x = input()

for i in range(len(x)):
  if(dc[x[i]] == -1):
    dc[x[i]] = i

for key in dc:
  print(dc[key], end = " ")