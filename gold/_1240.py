import sys
input = sys.stdin.readline

def search(nodes, t1, t2):
  def dfs(cur, parent, target, dist):
    if cur == target:
      return dist
    
    for nxt, d in nodes[cur]:
      if nxt != parent:
        ret = dfs(nxt, cur, target, dist + d)
        if ret != -1:
          return ret
    
    return -1

  ret = dfs(t1, None, t2, 0)
  return ret

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
nodes[0] = None
for _ in range(n-1):
  s, e, w = map(int, input().split())
  nodes[s].append((e, w))
  nodes[e].append((s, w))

ans = []
for _ in range(m):
  t1, t2 = map(int, input().split())
  ans.append(search(nodes, t1, t2))

print("\n".join(map(str, ans)))
