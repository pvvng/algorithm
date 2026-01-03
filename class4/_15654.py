import sys
input = sys.stdin.readline

def permutation(arr, k):
  ret = []
  path = []
  visited = [False] * len(arr)

  def dfs():
    if len(path) == k:
      ret.append(list(path))
      return 
    
    for i in range(len(arr)):
      if visited[i]:
        continue
      path.append(arr[i])
      visited[i] = True
      dfs()
      path.pop()
      visited[i] = False

  dfs()

  return ret

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
for l in permutation(A, m):
  ans.append(" ".join(map(str, l)))

print("\n".join(ans))