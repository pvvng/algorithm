import sys
input = sys.stdin.readline

def mul(iter):
  res = 1
  for i in iter:
    res *= i
  return res

def get_joined(iter):
  return " ".join(map(str, iter))

def dfs(B, n, pa, pb):
  # 최초로 등장하는 [-1]인 아닌 조합이 정답이다
  if len(B) == n:
    return B[:] if pa < pb else [-1]

  for i in range(1, 10):
    B.append(i)
    res = dfs(B, n, pa, pb * i)
    B.pop()
    if res[0] != -1:
      return res
  
  return [-1]

def sol(n, A):
  A.sort()
  B = []
  return get_joined(dfs(B, n, mul(A), 1))

n = int(input())
A = list(map(int, input().split()))
print((sol(n, A)))