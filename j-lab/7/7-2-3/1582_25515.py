import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur, total, tree, weight):
  ans = weight[cur] + total
  for nxt in tree[cur]:
    # dfs를 하는게 이득인 상황일때만 가산
    ans += max(0, dfs(nxt, total, tree, weight))
  return ans

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
w = list(map(int, input().split()))
print(dfs(0, 0, tree, w))