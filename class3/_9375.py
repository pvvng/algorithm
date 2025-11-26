def sol(C):
  d = {}
  for _, type in C:
    d.setdefault(type, 0)
    d[type] += 1
  res = 1
  for key in d:
    res *= d[key] + 1
  return res - 1

ans = []
t = int(input())
for _ in range(t):
  C = [input().split() for _ in range(int(input()))]
  ans.append(str(sol(C)))
print("\n".join(ans))
