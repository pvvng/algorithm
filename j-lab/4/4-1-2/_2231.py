import sys
input = sys.stdin.readline

def sol(n: int):
  ans = 0
  for i in range(n):
    if n == sum(list(map(int, list(str(i))))) + i:
      ans = i
      break
  return ans

n = int(input())
print(sol(n))