MIN = 0
MAX = 100000

def sol(n, k):
  dist = [-1] * (MAX + 1)
  dist[n] = 0  

  q = [n]
  idx = 0
  while idx < len(q):
    cur = q[idx]
    idx += 1

    if cur == k:
      return dist[cur]

    nxt = cur * 2
    if nxt <= MAX and dist[nxt] == -1:
      dist[nxt] = dist[cur]
      q.append(nxt)
    
    for nxt in [cur-1, cur+1]:
      if MIN <= nxt <= MAX and dist[nxt] == -1:
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

n, k = map(int, input().split())
print(sol(n, k))