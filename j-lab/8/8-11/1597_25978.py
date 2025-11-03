import sys
input = sys.stdin.readline

def sol(n, A, B):
  diff = [[0] * (n + 1) for _ in range(n + 1)]
  query_2 = []
  for b in B:
    q, i1, j1, i2, j2, *rest = b
    if q == 1:
      k = rest[0]
      diff[i1][j1] += k
      diff[i1][j2+1] -= k
      diff[i2+1][j1] -= k
      diff[i2+1][j2+1] += k
    else:
      query_2.append((i1, j1, i2, j2))

  # diff 더하기
  for r in range(n):
    for c in range(1, n):
      diff[r][c] += diff[r][c-1]
  
  for c in range(n):
    for r in range(1, n):
      diff[r][c] += diff[r-1][c]

  for i in range(n):
    for j in range(n):
      A[i][j] += diff[i][j]

  # 열 누적합
  for r in range(n):
    for c in range(1, n):
      A[r][c] += A[r][c-1]

  # 행 누적합
  for c in range(n):
    for r in range(1, n):
      A[r][c] += A[r-1][c]

  ans = []
  for i1, j1, i2, j2 in query_2:
    sum = A[i2][j2]
    if i1 > 0: sum -= A[i1-1][j2]
    if j1 > 0: sum -= A[i2][j1-1]
    if i1 > 0 and j1 > 0: sum += A[i1-1][j1-1]
    ans.append(str(sum))

  return "\n".join(ans)

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
print(sol(n, A, B))