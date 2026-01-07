a, b = map(int, input().split())

idx = 0
q = [(a, 1)]

mod = [1, 2]

ans = -1

while idx < len(q):
  cur, dist = q[idx]
  idx += 1

  if cur == b:
    ans = dist
    break

  for m in mod:
    if m == 1:
      nxt = int(str(cur) + str(m))
      if nxt > b:
        continue
      q.append((nxt, dist+1))
    if m == 2:
      nxt = cur * m
      if nxt > b:
        continue
      q.append((nxt, dist+1))
    
print(ans)