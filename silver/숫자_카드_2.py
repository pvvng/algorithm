import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
# 가진 숫자 카드
ls_1 = input().split()
m = int(input())
# 구해야할 숫자카드
ls_2 = input().split()

dct = defaultdict(int)
for v in ls_1:
  dct[v] += 1

for e in ls_2:
  print(dct[e], end=" ")