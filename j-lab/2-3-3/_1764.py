import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
N = set(input() for _ in range(n))
M = set(input() for _ in range(m))
ans = N&M
print(len(ans))
for e in sorted(ans):
  print(e)
