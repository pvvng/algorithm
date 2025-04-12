import sys
input = sys.stdin.readline

n = int(input())

ls = []
for _ in range(n):
  ls.append(tuple(map(int, input().split())))

for v in sorted(ls, key=lambda x : (x[1], x[0])):
  print(f"{v[0]} {v[1]}")