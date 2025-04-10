n = int(input())

mt = 1
for i in range(1, n+1):
  mt *= i

cnt = 0
mt = str(mt)
for i in range(len(mt)):
  if(mt[len(mt) - i - 1] == "0"):
    cnt += 1
  else:
    break
print(cnt)