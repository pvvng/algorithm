import sys
sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
  l = list(map(int, input().split())) 
  for j in range(n):
    if l[j] == 1:
      graph[i].append(j)

visited = [[False] * n for _ in range(n)]
for i in range(n):
  def dfs(cur):
    for j in graph[cur]:
      if not visited[i][j]:
        visited[i][j] = True
        dfs(j)
  dfs(i)

ans = []
for i in range(n):
  l = []
  for j in range(n):
    l.append(str(int(visited[i][j])))
  ans.append(" ".join(l))

print("\n".join(ans))
