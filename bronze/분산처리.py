import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
  a, b = map(int, input().split())
  res = pow(a, b, 10)
  if res == 0:
    res = 10
  ans.append(res)

print("\n".join(map(str, ans)))