import sys
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
  ls.append(tuple(map(int, input().split())))

ls.sort(key=lambda x : x)

for v in ls:
  print(f"{v[0]} {v[1]}")