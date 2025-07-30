def sol(A:list, n: int, k:int) -> int:
  idx = n
  for i in range(n):
    if A[i] >= k:
      idx = i
      break
  return n - idx

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(m):
  k = int(input())
  print(sol(A, n, k))
