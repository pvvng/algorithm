import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knows = list(map(int, input().split()))[1:]

linked = [[] for _ in range(n+1)]
linked[0] = None

# parties[i] = 사람 i가 참석하는 파티 리스트
parties = [[] for _ in range(n+1)]
parties[0] = None

for k in range(1, m + 1):
  party = list(map(int, input().split()))[1:]
  for i in range(len(party)):
    p1 = party[i]
    parties[p1].append(k)
    for j in range(len(party)):
      p2 = party[j]
      if p1 == p2:
        continue
      linked[p1].append(p2)

# 연결된 사람 dfs로 탐색하여 연결
total_linked = set()
def dfs(cur, visited):
  total_linked.add(cur)
  for nxt in linked[cur]:
    if not visited[nxt]:
      visited[nxt] = True
      dfs(nxt, visited)

for k in knows:
  dfs(k, [False] * (n+1))

lie = [True] * (m + 1)
lie[0] = False
for tl in total_linked:
  cant = parties[tl]
  for p in cant:
    lie[p] = False

print(lie.count(True))