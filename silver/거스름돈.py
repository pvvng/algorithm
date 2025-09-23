def sol(n: int):
  dd = [2, 5]
  q = [(n, 0)]
  visited = [False] * 100001
  idx = 0
  while idx < len(q):
    cur = q[idx]
    idx += 1
    if cur[0] == 0:
      return cur[1]
    for d in dd:
      if cur[0] - d >= 0 and not visited[cur[0] - d]:
        q.append((cur[0] - d, cur[1] + 1))
        visited[cur[0] - d] = True
  return -1

n = int(input())
print(sol(n))
