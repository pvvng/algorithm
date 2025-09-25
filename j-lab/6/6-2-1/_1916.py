import sys
input = sys.stdin.readline
from queue import PriorityQueue
Inf = float("inf")

def sol(n, edges, a, b):
  e = [[] for _ in range(n+1)]
  for u, v, w in edges:
    e[u].append([v, w])
  return dijkstra(n, e, a, b)

def dijkstra(n, e, a, b):
  dist = [Inf] * (n + 1)
  selected = [False] * (n + 1)
  pq = PriorityQueue()

  dist[a] = 0
  pq.put([0, a])

  while not pq.empty():
    cost, cur = pq.get()
    if selected[cur] or dist[cur] < cost:
      continue
    selected[cur] = True
    if cur == b:
      return dist[cur]
    for nxt, c in e[cur]:
      nxt_dist = cost + c
      if not selected[nxt] and dist[nxt] > nxt_dist:
        dist[nxt] = nxt_dist
        pq.put([nxt_dist, nxt])

  return -1
  
n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
a, b = map(int, input().split())
print(sol(n, edges, a, b))
