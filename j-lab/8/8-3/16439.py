import sys
input = sys.stdin.readline

def combinations(arr, r):
  result = []
  path = []

  def dfs(start):
    if len(path) == r:
      result.append(tuple(path))
      return
    for i in range(start, len(arr)):
      path.append(arr[i])
      dfs(i + 1)
      path.pop()

  dfs(0)
  return result

def sol(m, A):
  arr = [i for i in range(m)]
  ans = 0
  for i, j, k in combinations(arr, 3):
    s = 0
    for a in A:
      s += max(a[i], a[j], a[k])
    if s > ans:
      ans = s
  return ans

n, m = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
print(sol(m, A))
