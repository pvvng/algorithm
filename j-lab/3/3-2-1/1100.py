def sol(A: str, k: int) -> str:
  while len(A) < k:
    A += A[-1]
  return A

def sol2(A, k):
  A += A[-1] * (k - len(A))
  return A

A = input().strip()
k = int(input())
print(sol(A, k))
