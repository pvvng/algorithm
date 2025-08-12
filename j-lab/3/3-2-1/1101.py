def sol(A:str, k:int):
  while len(A) < k:
    A = A[0] + A
  return A

A = input().strip()
k = int(input())
print(sol(A, k))