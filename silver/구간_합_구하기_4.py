import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
prefix = [0] * (len(ls) + 1)

for i in range(len(ls)):
  prefix[i+1] = ls[i] + prefix[i]

for _ in range(m):
  strt, end = map(int, input().split())
  print(prefix[end] - prefix[strt - 1])
