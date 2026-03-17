import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
  s, e = map(int, input().split())
  ret = 0
  for i in range(s, e+1):
    ret += str(i).count("0")
  ans.append(str(ret))
print("\n".join(ans))