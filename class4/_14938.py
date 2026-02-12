import sys
import heapq
input = sys.stdin.readline

inf = float("inf")

# 100, 15, 10
n, m, r = map(int, input().split())
t = [None] + list(map(int, input().split()))

table = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  table[i][i] = 0

# 100
for _ in range(r):
  p, c, w = map(int, input().split())
  table[p][c] = w
  table[c][p] = w

ans = [0] * (n+1)

# 플로이드 워셜
# i->j vs i->k->j 중 최단 경로
# q. 최단거리를 업데이트 한 뒤에 i->t->j
# 중간노드 t의 가치를 더해야 하지 않나?
# a. i->t->j 가 가능했다면 
# 자연스럽게 i->t 도 이후 누계에서 계산됨 
# 고로 생각할 필요 X
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      table[i][j] = min(table[i][j], table[i][k] + table[k][j])

# 시작점 i -> j
# i -> t -> j (플로이드 워셜)
for i in range(1, n+1):
  ret = 0
  for j in range(1, n+1):
    # 이동 불가
    if table[i][j] == inf or table[i][j] > m:
      continue  
    ret += t[j]
  ans[i] = ret

print(max(ans))
