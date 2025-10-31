import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
# 열 누적합
for r in range(n):
  for c in range(1, m):
    A[r][c] += A[r][c-1]

# 행 누적합
for c in range(m):
  for r in range(1, n):
    A[r][c] += A[r-1][c]

k = int(input())
ans = []
for _ in range(k):
  i, j, x, y = map(int, input().split())
  i -= 1; j -= 1; x -= 1; y -= 1
  sum = A[x][y]
  if i > 0: sum -= A[i-1][y]
  if j > 0: sum -= A[x][j-1]
  if i > 0 and j > 0: sum += A[i-1][j-1]
  ans.append(str(sum))

print("\n".join(ans))
