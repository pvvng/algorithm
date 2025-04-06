import sys
input=sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
  ls.append(int(input()))
for v in sorted(ls):
  print(v)