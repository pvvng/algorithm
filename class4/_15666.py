import sys
input = sys.stdin.readline

def permutation(arr, k):
  ret = []
  path = []
  def dfs(prev):
    if len(path) == k:
      ret.append(" ".join(map(str, path)))
      return
    for i in range(len(arr)):
      if prev <= arr[i]:
        path.append(arr[i])
        dfs(arr[i])
        path.pop()
  dfs(-1)

  return ret

n, m = map(int, input().split())
A = list(set(list(map(int, input().split()))))
A.sort()

print("\n".join(permutation(A, m)))