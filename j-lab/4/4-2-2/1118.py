import sys
sys.setrecursionlimit(10**6)

def sol1(n: int):
  if n == 1:
    return 1
  return n + sol1(n - 1)

def sol2(n: int):
  sum([i + 1 for i in range(n)])

def sol3(n: int):
  return n * (n + 1) // 2

n = int(input())