def permutation(arr, k):
  ret = []
  path = []
  visited = [False] * len(arr)
  has = set()

  def dfs():
    if len(path) == k:
      p = " ".join(map(str, path))
      if p not in has:
        ret.append(p)
        has.add(p)
      return 
    for i in range(len(arr)):
      if visited[i]:
        continue
      visited[i] = True
      path.append(arr[i])
      dfs()
      visited[i] = False
      path.pop()
  
  dfs()
  return ret

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

print("\n".join(permutation(A, m)))