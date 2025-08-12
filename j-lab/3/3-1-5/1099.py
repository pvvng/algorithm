def sol(A: list, T:tuple):
  t, i1, j1, i2, j2, *rest = T

  if t == 1:
    k = rest[0]
    for i in range(i1, i2 + 1):
      for j in range(j1, j2 + 1):
        A[i][j] += k
  else:
    cnt = 0
    for i in range(i1, i2 + 1):
      for j in range(j1, j2 + 1):
        cnt += A[i][j]
    print(cnt)

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
  T = tuple(map(int, input().split()))
  sol(A, T)