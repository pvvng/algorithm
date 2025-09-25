from queue import PriorityQueue

Infinity = float('inf')

def sol(n: int, edges: list, x: int, z: int):
  E = [[] for _ in range(n+1)]
  for u, v, w in edges:
    E[u].append([v, w])
  return dijkstra(n, E, x, z)

def dijkstra(n: int, e: list, x: int, z: int):
  dist = [Infinity] * (n + 1)
  selected = [False] * (n + 1)
  pq = PriorityQueue()

  dist[x] = 0
  pq.put([0, x])

  while not pq.empty():
    cost, cur = pq.get()
    if selected[cur] or dist[cur] < cost:
      continue
    selected[cur] = True
    if cur == z:
      return dist[cur]
    for nxt, c in e[cur]:
      nxt_dist = cost + c
      if not selected[nxt] and nxt_dist < dist[nxt]:
        dist[nxt] = nxt_dist
        pq.put([nxt_dist, nxt])

# 정점의 수 N, 간선의 수 M
n, m = map(int, input().split())
# 간선 정보 u, v, w:  도시 u에서 도시 v로 가중치가 w
edges = [list(map(int, input().split())) for _ in range(m)]
# 출발 정점 X와 도착 정점 Z
x, z = map(int, input().split())
print(sol(n, edges, x, z))