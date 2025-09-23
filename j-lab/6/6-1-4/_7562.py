import sys
input = sys.stdin.readline

def in_range(l, r, c):
  return 0 <= r < l and 0 <= c < l 

def sol(l: int, loc:tuple[int, int], target: tuple[int, int]):
  dt = [(2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
  visited = list([False] * l for _ in range(l))
  q = [(loc[0], loc[1], 0)]
  visited[loc[0]][loc[1]] = True
  idx = 0
  while idx < len(q):
    r, c, d = q[idx]
    idx += 1

    if target[0] == r and target[1] == c:
      return d

    for dr, dc in dt:
      nr = r + dr; nc = c + dc
      if not in_range(l, nr, nc):
        continue
      if not visited[nr][nc]:
        q.append((nr, nc, d + 1))
        visited[nr][nc] = True

ans = []
for _ in range(int(input())):
  l = int(input())
  loc = tuple(map(int, input().split()))
  target = tuple(map(int, input().split()))
  ans.append(sol(l, loc, target))

print("\n".join(map(str, ans)))