from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)

for _ in range(n):
  x = int(input())
  dic[x] += 1

key_sort = list(sorted(dic.items()))

for (v, i) in key_sort:
  for j in range(i):
    print(v)