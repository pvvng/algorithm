import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def bfs(i, target):
  q = [(i, 0)]
  idx = 0
  visited = [False] * (n+1)
  visited[i] = 0

  while idx < len(q):
    cur, num = q[idx]
    idx += 1

    if cur == target:
      return num
    
    for nxt in graph[cur]:
      if nxt == target:
        return num + 1
      
      if not visited[nxt]:
        visited[nxt] = True
        q.append((nxt, num+1))

res = []
for i in range(1, n+1):
  bacon = 0
  for j in range(1, n+1):
    if i == j: continue
    bacon += bfs(i, j)
  res.append((i, bacon))
res.sort(key=lambda x : (x[1], x[0]))
print(res[0][0])