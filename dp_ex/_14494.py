n, m = map(int, input().split())
A = [[1] * m for _ in range(n)]

for i in range(1, n):
  for j in range(1, m):
    A[i][j] = (A[i-1][j] + A[i][j-1] + A[i-1][j-1]) % 1000000007

print(A[n-1][m-1] % 1000000007)