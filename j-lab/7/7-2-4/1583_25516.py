import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(k, tree, w, cur, depth):
  # depth가 k 이하인 애들만 카운트
  if depth > k:
    return 0
  total = w[cur]
  for nxt in tree[cur]:
    total += dfs(k, tree, w, nxt, depth + 1)
  return total

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
w = list(map(int, input().split()))
print(dfs(k, tree, w, 0, 0))