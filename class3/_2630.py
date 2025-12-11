import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(B, loc):
  res = [0, 0]
  x, y, scope = loc

  start = B[x][y]
  is_confetti = True
  for i in range(x, x + scope):
    for j in range(y, y + scope):
      if B[i][j] != start:
        is_confetti = False
        break

  if is_confetti:
    temp = [0, 0]
    temp[start] += 1
    return temp

  ns = scope // 2
  dt = [(0, 0), (0, ns), (ns, 0), (ns, ns)]
  for dx, dy in dt:
    nx = x + dx; ny = y + dy
    ret = sol(B, (nx, ny, ns))
    res[0] += ret[0]
    res[1] += ret[1]
  
  return res

n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
ans = sol(B, (0, 0, n))
print("\n".join(map(str, ans)))