n = int(input())
A = list(map(int, input().split()))
i, j, k = map(int, input().split())

def multiply(A: list, start: int, end:int, dx: int):
  for i in range(start, end + 1):
    A[i] *= dx
  return sum(A)

print(multiply(A, i, j, k))