def sol(A:list, T:list[list[int, int]]):
  for idx in range(1, n):
    A[idx] += A[idx - 1]

  for i, j in T:
    if i == 1:
      print(A[j-1])
    else:
      print(A[j-1] - A[i-1-1])
    
n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(m)]
sol(A, T)