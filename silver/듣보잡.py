import sys
input = sys.stdin.readline

n, m = map(int, input().split())

듣잡 = set()
보잡 = set()

for _ in range(n):
  듣잡.add(input().replace("\n", ""))

for _ in range(m):
  보잡.add(input().replace("\n", ""))

듣보잡 = 듣잡 & 보잡
print(len(듣보잡))
for i in sorted(듣보잡):
  print(i)