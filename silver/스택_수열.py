import sys
input = sys.stdin.readline

n = int(input())

ks = []
for _ in range(n):
  ks.append(int(input()))

stk = []
ans = []
idx = 1
for x in ks:
  for i in range(idx, x + 1):
    stk.append(i)
    ans.append("+")
    idx = x + 1
  if len(stk) > 0 and stk[-1] == x:
    stk.pop()
    ans.append("-")

if len(stk) > 0:
  print("NO")
else:
  for v in ans:
    print(v)
