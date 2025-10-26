import sys
input = sys.stdin.readline

ans = []
for _ in range(3):
  x = int(input())
  res = 0
  for _ in range(x):
    res += int(input())
  if res > 0:
    ans.append("+")
  elif res < 0:
    ans.append("-")
  else:
    ans.append("0")
print("\n".join(ans))