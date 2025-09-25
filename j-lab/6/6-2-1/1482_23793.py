# x -> y -> z
# x -> y 로 가는 최단 경로 구하고 y -> z 로 가는 최단 경로 구한뒤 둘이 더하기

# 출발 정점 X에서 출발하여 중간 정점 Y를 거치지 않고 도착 정점 Z에 도달하는 최단 거리
# -> y를 이미 방문한 것으로 설정

import sys
input = sys.stdin.readline

from queue import PriorityQueue
Infinity = float('inf')

def sol(n, edges, x, y, z):
  e = [[] for _ in range(n + 1)]
  for u, v, w in edges: # 도시 u에서 도시 v로 가중치가 정수 w인 도로
    e[u].append([v, w])

  x_to_y = dijkstra(n, e, x, y)
  y_to_z = dijkstra(n, e, y, z)
  ans1 = x_to_y + y_to_z

  if x_to_y == -1 or y_to_z == -1:
    ans1 = -1
  
  ans2 = dijkstra(n, e, x, z, [y])

  return f"{ans1} {ans2}"

def dijkstra(n, e, start, end, not_visit = []):
  dist = [Infinity] * (n+1) # 최단거리 배열
  selected = [False] * (n+1)
  pq = PriorityQueue()

  dist[start] = 0
  pq.put([0, start])

  # 방문하지 않을 노드 방문처리
  for nx in not_visit:
    selected[nx] = True

  while not pq.empty():
    cost, cur = pq.get()

    # 현재 이동 비용보다 단거리인 경로가 존재하면 무시
    if selected[cur] or dist[cur] < cost: 
      continue

    selected[cur] = True # 이동

    if cur == end:
      return dist[cur]

    for nxt, c in e[cur]:
      nxt_dist = cost + c
      # 현재 이동 비용이 기록된 경로보다 적으면 업데이트
      if not selected[nxt] and nxt_dist < dist[nxt]:
        dist[nxt] = nxt_dist
        pq.put([nxt_dist, nxt])

  return -1

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
x, y, z = map(int, input().split())
print(sol(n, edges, x, y, z))