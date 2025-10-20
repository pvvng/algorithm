import sys
input = sys.stdin.readline

n = int(input())
ss = input().split()
stu = {}
for s in ss:
  stu.setdefault(s, 0)
for _ in range(n):
  loving = input().split()
  for l in loving:
    stu[l] += 1
res = []
for key in stu:
  res.append((key, stu[key]))
res.sort(key=lambda x : (-x[1], x[0]))
ans = list(map(lambda x : f"{x[0]} {x[1]}", res))
print("\n".join(ans))