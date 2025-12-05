x = input()
res = []
for o in x.split("-"):
  res.append(sum(map(int, o.split("+"))))
ans = res[0]
for i in range(1, len(res)):
  ans -= res[i]
print(ans)