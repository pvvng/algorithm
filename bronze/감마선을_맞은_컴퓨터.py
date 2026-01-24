import sys
input = sys.stdin.readline

ans = ""
for _ in range(15):
  x = input().split()
  if "w" in x:
    ans = "chunbae"
  if "b" in x:
    ans = "nabi"
  if "g" in x:
    ans = "yeongcheol"
print(ans)