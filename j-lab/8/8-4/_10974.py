def sol(n):
  arr = [i for i in range(1, n+1)]

  res = []
  path = []
  visited = [False] * n

  def dfs():
    if len(path) == n:
      res.append(" ".join(path))
      return
    
    for i in range(n):
      if not visited[i]:
        path.append(str(arr[i]))
        visited[i] = True
        dfs()
        path.pop()
        visited[i] = False
  
  dfs()
  return sorted(res)

n = int(input())
print("\n".join(sol(n)))