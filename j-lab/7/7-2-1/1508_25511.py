import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n, edges, nodes, k):
  tree = [[] for _ in range(n)]
  for p, c in edges:
    tree[p].append(c)

  return dfs(0, nodes, k, tree, 0)

def dfs(cur: int, nodes: list, target: int, tree: list, deps: int):
  if nodes[cur] == target:
    return deps

  for nxt in tree[cur]:
    found = dfs(nxt, nodes, target, tree, deps + 1)
    if found != -1: 
      return found
  return -1
  
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
nodes = list(map(int, input().split()))
print(sol(n, edges, nodes, k))
