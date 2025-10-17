import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
  t = input()
  if t[0] == "P":
    ans.append("skipped")
  else:
    a, b = map(int, t.split("+"))
    ans.append(str(a + b))
print("\n".join(ans))