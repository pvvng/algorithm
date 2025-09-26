import sys, heapq
from itertools import permutations

input = sys.stdin.readline
Inf = float("inf")
  
def dijkstra(n, e, start):
  dist = [Inf] * (n + 1)
  pq = [(0, start)]
  dist[start] = 0

  while len(pq) > 0:
    cost, cur = heapq.heappop(pq)
    if cost > dist[cur]:
      continue
    for nxt, c in e[cur]:
      nxt_dist = cost + c
      if dist[nxt] > nxt_dist:
        dist[nxt] = nxt_dist
        heapq.heappush(pq, (nxt_dist, nxt))

  return dist

def permutation(mid_edges):
  p = []
  for a in mid_edges:
    for b in mid_edges:
      if a == b: continue
      for c in mid_edges:
        if c == b or c == a: continue
        p.append((a, b, c))
  return p

n, m = map(int, input().split())
e = [[] for _ in range(n+1)]
for i in range(m):
  u, v, w = map(int,input().split())
  e[u].append((v,w))
  e[v].append((u,w))

x, z = map(int, input().split()) # 출발, 도착
p = int(input()) # 중간 정점 개수
mid_edges = list(map(int, input().split()))

dists = {}
for mid in mid_edges:
  dists[mid] = dijkstra(n, e, mid)
dists[x] = dijkstra(n, e, x)

ans = Inf
for a, b, c in permutations(mid_edges, 3):
  total = dists[x][a] + dists[a][b] + dists[b][c] + dists[c][z]
  if ans > total:
    ans = total

if ans == Inf: print(-1)
else: print(ans)