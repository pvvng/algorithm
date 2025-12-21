import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
  _, d = input().split("-")
  d = int(d)
  ans += int(d <= 90)
print(ans)
