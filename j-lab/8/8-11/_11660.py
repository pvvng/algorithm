import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# 누적합 구하기
for r in range(n):
  for c in range(1, n):
    A[r][c] += A[r][c-1]

for c in range(n):
  for r in range(1, n):
    A[r][c] += A[r-1][c]

ans = []
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  x1 -=1; x2 -= 1; y1 -= 1; y2 -= 1
  sum = A[x2][y2]
  if x1 > 0: sum -= A[x1-1][y2]
  if y1 > 0: sum -= A[x2][y1-1]
  if x1 > 0 and y1 > 0: sum += A[x1-1][y1-1]
  ans.append(str(sum))

print("\n".join(ans))
