ans = (-1, -1)
for i in range(5):
  t = sum(list(map(int, input().split())))
  if ans[1] < t:
    ans = (i+1, t)
print(*ans)