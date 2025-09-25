import sys
input = sys.stdin.readline

from queue import PriorityQueue
INF = float("inf")

def sol(V: int, k: int, edges: list[list[int]]):
  e = [[] for _ in range(V + 1)]
  for u, v, w in edges:
    e[u].append([v, w])

  ans = []
  for d in dijkstra(V, k, e):
    if d == INF:
      ans.append("INF")
    else:
      ans.append(str(d))
  return ans

def dijkstra(v, start, e):
  dist = [INF] * (v + 1)
  selected = [False] * (v + 1)
  pq = PriorityQueue()

  dist[start] = 0
  pq.put([0, start])

  while not pq.empty():
    cost, cur = pq.get()
    if selected[cur] or dist[cur] < cost:
      continue
    selected[cur] = True
    for nxt, c in e[cur]:
      nxt_dist = cost + c
      if not selected[nxt] and dist[nxt] > nxt_dist:
        dist[nxt] = nxt_dist
        pq.put([nxt_dist, nxt])

  return dist[1:]

v, e = map(int, input().split()) # 정점의 개수 V와 간선의 개수 E
k = int(input()) # 시작 정점의 번호 K
edges = [list(map(int, input().split())) for _ in range(e)] # u -> v: w
print("\n".join(sol(v, k, edges)))