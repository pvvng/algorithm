def sol(n, A):
  tree = {}
  for i in range(1, n+1):
    tree.setdefault(i, [])
  for a in A:
    tree[a[0]].append(a[1])
    tree[a[1]].append(a[0]) # “네트워크/케이블” 문제면: 한쪽에서 연결되면 당연히 반대쪽에서도 연결된 거라서 양방향.

  idx = 0
  queue = [1]
  visited = {1}
  while idx < len(queue):
    crt = queue[idx]
    idx += 1
    for nxt in tree[crt]:
      if nxt not in visited:
        queue.append(nxt)
        visited.add(nxt)

  visited.remove(1)
  return len(visited)

n = int(input())
m = int(input())
A = [list(map(int, input().split())) for _ in range(m)]
print(sol(n, A))