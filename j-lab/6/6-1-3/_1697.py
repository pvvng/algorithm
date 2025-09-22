def in_range(n):
  return 0 <= n <= 100000

def sol(n:int, k:int):
  dt = [("+", 1), ("+", -1), ("*", 2)]
  q = [(n, 0)]
  idx = 0
  visited = [False] * 100001
  visited[n] = True
  while True:
    crt, move = q[idx]
    idx += 1
    if crt == k:
      return move
    for op, val in dt:
      if op == "+" and in_range(crt + val) and not visited[crt+val]:
        q.append((crt + val, move + 1))
        visited[crt+val] = True
      if op == "*" and in_range(crt * val) and not visited[crt*val]:
        q.append((crt * val, move + 1))
        visited[crt*val] = True

n, k = map(int, input().split())
print(sol(n, k))