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
order = [0] * n
depth = [-1] * n

q = [r - 1]
visited[r - 1] = True
idx = 0
depth[r - 1] = 0

while idx < len(q):
  cur = q[idx]
  idx += 1
  order[cur] = idx
  for nxt in tree[cur]:
    if not visited[nxt]:
      depth[nxt] = depth[cur] + 1
      visited[nxt] = True
      q.append(nxt)

ans = 0
for i in range(n):
  ans += order[i] * depth[i]
print(ans)