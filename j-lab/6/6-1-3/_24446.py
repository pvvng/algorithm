import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
tree = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)

for u in tree:
  u.sort()

visited = [False] * n
depth = [-1] * n

q = [r-1]
visited[r-1] = True
depth[r-1] = 0

idx = 0
while idx < len(q):
  cur = q[idx]
  idx += 1
  for nxt in tree[cur]:
    if not visited[nxt]:
      visited[nxt] = True
      depth[nxt] = depth[cur] + 1  # 부모 깊이 + 1
      q.append(nxt)

print("\n".join(map(str, depth)))