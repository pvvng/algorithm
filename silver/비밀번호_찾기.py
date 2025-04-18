import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dct = {}
for _ in range(n):
  web, pw = input().split()
  dct.setdefault(web, pw)

for _ in range(m):
  print(dct.get(input().strip()))
