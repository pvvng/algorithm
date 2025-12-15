m = int(input())
n = int(input())
ans = []
for i in range(m, n+1):
  t = i ** 0.5
  if t == int(t):
    ans.append(i)
if len(ans) == 0:
  print(-1)
else:
  print(sum(ans))
  print(ans[0])
