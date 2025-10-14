import sys
input = sys.stdin.readline

def sol(nodes, n, v):
  for en in nodes:
    en.sort()

  dfs_res = join_list(dfs(nodes, v, [], [False] * (n+1)))
  bfs_res = join_list(bfs(nodes, v, n))

  return dfs_res + "\n" + bfs_res

def dfs(nodes, cur, order, visited):
  visited[cur] = True
  order.append(str(cur))
  for nxt in nodes[cur]:
    if not visited[nxt]:
      dfs(nodes, nxt, order, visited)
  return order

def bfs(nodes, v, n):
  q = [v]
  visited = [False] * (n+1)
  visited[v] = True

  idx = 0
  order = []
  while idx < len(q):
    cur = q[idx]
    order.append(str(cur))
    idx += 1  
    for nxt in nodes[cur]:
      if not visited[nxt]:
        q.append(nxt)
        visited[nxt] = True
  return order

def join_list(list):
  return " ".join(list)

n, m, v = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
  p, c = map(int, input().split())
  nodes[p].append(c)
  nodes[c].append(p)

print(sol(nodes, n, v))