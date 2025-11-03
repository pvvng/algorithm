import sys
input = sys.stdin.readline

def sol(n, A):
  mx = get_maxy(A)

  # 누적합 구하기
  for r in range(n):
    for c in range(1, n):
      A[r][c] += A[r][c-1]

  for c in range(n):
    for r in range(1, n):
      A[r][c] += A[r-1][c]

  ans = []
  for d in range(n + 1):
    ans.append(solve(n, d, A, mx))
  return max(ans)

# 요소 중 최댓값 구하기
def get_maxy(A):
  mx = -1001
  for a in A:
    if mx < max(a):
      mx = max(a)
  return mx

def solve(n, d, A, mx):
  res = mx
  for r1 in range(n - d):
    for c1 in range(n - d):
      # (r, c) ~ (r+d, c+d)
      r2, c2 = r1+d, c1+d
      sum = A[r2][c2]
      if r1 > 0: sum -= A[r1-1][c2]
      if c1 > 0: sum -= A[r2][c1-1]
      if r1 > 0 and c1 > 0: sum += A[r1-1][c1-1]
      # 최댓값 변경
      if res < sum:
        res = sum
  return res

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, A))