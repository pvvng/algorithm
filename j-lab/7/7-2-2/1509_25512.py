import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n, edges, cost):
  tree = [[] for _ in range(n)]
  for p, c in edges:
    tree[p].append(c)

  return min(dfs(0, tree, 0, cost), dfs(0, tree, 1, cost))

def dfs(cur, tree, color, cost):
  ret = cost[cur][color]
  for nxt in tree[cur]:
    ret += dfs(nxt, tree, 1 - color, cost)
  return ret

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
cost = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, edges, cost))