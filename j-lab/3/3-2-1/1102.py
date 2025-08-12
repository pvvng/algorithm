def sol(A:str, k:int):
  A = A[0] * (k - len(A)) + A
  return A

A = input().strip()
k = int(input())
print(sol(A, k))