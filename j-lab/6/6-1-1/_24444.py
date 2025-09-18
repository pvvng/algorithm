import sys
input = sys.stdin.readline

def sol(n, T, r):
  adj = [[] for _ in range(n + 1)]
  for a, b in T:
    adj[a].append(b)
    adj[b].append(a)

  for v in range(1, n + 1):
    adj[v].sort()

  # 입력 크기 N이 매우 크고 단순 타입(예: int, 작은 범위 인덱스)만 다룸 
  # -> set/dict 대신 리스트/배열이 압도적으로 빠름.
  visited = [False] * (n + 1)
  order = [0] * (n + 1)

  q = [r]
  visited[r] = True

  idx = 0
  while idx < len(q):
    crt = q[idx]
    idx += 1
    order[crt] = idx

    for nxt in adj[crt]:
      if not visited[nxt]:
        q.append(nxt)
        visited[nxt] = True

  return order[1:]

# 정점의 수 N, 간선의 수 M, 시작 정점 r
# 가중치 1인 양방향 간선
n, m, r = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(m)]
ans = sol(n, T, r)
print('\n'.join(map(str, ans)))