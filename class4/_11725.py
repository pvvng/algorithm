import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n + 1)]
tree[0] = None

for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
  tree[c].append(p)

# --------BFS----------
def bfs(tree):
  idx = 0
  q = [1]

  visited = [False] * (n+1)
  visited[1] = True

  parent = [0] * (n+1)

  while idx < len(q):
    cur = q[idx]
    for nxt in tree[cur]:
      if visited[nxt]:
        continue
      parent[nxt] = cur
      visited[nxt] = True
      q.append(nxt)

    idx += 1

  return parent[2:]

# --------DFS----------
def dfs(tree):
  parent = [0] * (n + 1)
  visited = [False] * (n+1)

  def fn(tree, cur, visited):
    for nxt in tree[cur]:
      if visited[nxt]:
        continue
      parent[nxt] = cur
      visited[nxt] = True
      fn(tree, nxt, visited)

  visited = [False] * (n+1)
  fn(tree, 1, visited)

  return parent[2:]

print("\n".join(map(str, bfs(tree))))