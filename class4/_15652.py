import sys
input = sys.stdin.readline

def permutation(arr, k):
  ret = []
  path = []
  def dfs(prev: int):
    if len(path) == k:
      ret.append(list(path))
      return 
    
    for e in arr:
      if prev <= e:
        path.append(e)
        dfs(e)
        path.pop()

  dfs(-1)

  return ret

n, m = map(int, input().split())
ret = permutation([i for i in range(1, n+1)], m)
ans = []
for e in ret:
  ans.append(" ".join(map(str, e)))
print("\n".join(ans))
