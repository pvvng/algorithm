import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = float("inf")
table = [[inf] * (n+1) for _ in range(n+1)]
# 기본 테이블 세팅
for _ in range(m):
  a, b, c = map(int, input().split())
  table[a][b] = min(c, table[a][b])

# 자기 자신은 0
for i in range(1, n+1):
  table[i][i] = 0

# 플로이드-워셜
# i -> j
# k 노드를 거쳐가는 경우 vs i -> j 이동 중 최솟값 선택
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        table[i][j] = 0
        continue
      table[i][j] = min(table[i][j], table[i][k] + table[k][j])

# 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if table[i][j] == inf:
      print(0, end=" ")
    else:
      print(table[i][j], end=" ")
  print("")
