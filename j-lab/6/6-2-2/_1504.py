import sys, heapq

input = sys.stdin.readline
Inf = float("inf")

def sol(n, edges, u, v):
  e = [[] for _ in range(n + 1)]
  for a, b, c in edges:
    e[a].append([b, c])
    e[b].append([a, c])
  
  dist_start = [Inf] * (n + 1)
  dijkstra(e, 1, dist_start)
  dist_u = [Inf] * (n + 1)
  dijkstra(e, u, dist_u)
  dist_v = [Inf] * (n + 1)
  dijkstra(e, v, dist_v)

  # 1 -> u -> v -> n
  cand1 = dist_start[u] + dist_u[v] + dist_v[n]
  # 1 -> v -> u -> n
  cand2 = dist_start[v] + dist_v[u] + dist_u[n]

  ans = min(cand1, cand2)
  if ans == Inf:
    return - 1
  return ans

def dijkstra(e, start, dist):
  dist[start] = 0
  pq = []
  heapq.heappush(pq, [0, start])

  while len(pq) > 0:
    cost, cur = heapq.heappop(pq)
    if dist[cur] < cost:
      continue

    for nxt, c in e[cur]:
      nxt_d = cost + c
      if dist[nxt] > nxt_d:
        dist[nxt] = nxt_d
        heapq.heappush(pq, [nxt_d, nxt])

n, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
u, v = map(int, input().split())
print(sol(n, edges, u, v))