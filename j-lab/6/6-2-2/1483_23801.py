import sys
input = sys.stdin.readline

import heapq
Inf = float("inf")

def sol(n, edges, x, z, mid_edges):
  e = [[] for _ in range(n + 1)]
  for u, v, w in edges:
    e[u].append([v, w])
    e[v].append([u, w]) # 무방향 그래프
  
  # 출발 정점, 도착 정점에서 모든 정점에 대한 비용 산출
  dist_start = [Inf] * (n + 1)
  dijkstra(e, x, dist_start)
  dist_end = [Inf] * (n + 1)
  dijkstra(e, z, dist_end)

  ans = Inf
  for mid in mid_edges:
    ans = min(ans, dist_start[mid] + dist_end[mid])

  if ans == Inf:
    return -1
  return ans

def dijkstra(e, start, dist):
  pq = []

  dist[start] = 0
  heapq.heappush(pq, [0, start])

  while len(pq) > 0:
    cost, cur = heapq.heappop(pq)
    if dist[cur] < cost:
      continue

    for nxt, c in e[cur]:
      nxt_dist = cost + c
      if dist[nxt] > nxt_dist:
        dist[nxt] = nxt_dist
        heapq.heappush(pq, [nxt_dist, nxt])

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
x, z = map(int, input().split()) # 출발, 도착
p = int(input()) # 중간 정점 개수
mid_edges = list(map(int, input().split()))
print(sol(n, edges, x, z, mid_edges))