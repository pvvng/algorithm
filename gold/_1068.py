import sys
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
k = int(input())

def sol(n, k, parents):
  root = -1
  tree = [[] for _ in range(n)]

  for i in range(n):
    if parents[i] == -1:
      root = i
      continue
    if i != k:
      tree[parents[i]].append(i)

  # 루트를 삭제한 경우
  if root == k:
    return 0
  
  ans = 0
  def dfs(cur):
    nonlocal ans
    # leaf
    if len(tree[cur]) == 0:
      ans += 1
      return 
    
    for nxt in tree[cur]:
      dfs(nxt)

  dfs(root)

  return ans

print(sol(n, k, parents))