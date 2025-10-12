import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
  a, b = map(int, input().split())
  ans.append(str(a + b))
print("\n".join(ans))
