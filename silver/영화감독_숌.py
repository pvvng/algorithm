n = int(input())

cnt = 0
numv = 666
while True:
  if "666" in str(numv):
    cnt += 1
  if cnt == n:
    break
  numv += 1

print(numv)
