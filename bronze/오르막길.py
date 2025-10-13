ol = []
n = int(input())
L = list(map(int, input().split()))

temp = []
for l in L:
  if len(temp) == 0 or temp[-1] < l:
    temp.append(l)
  else:
    ol.append(temp[-1] - temp[0])
    temp = [l]

if len(temp) > 1:
  ol.append(temp[-1] - temp[0])

print(max(ol))