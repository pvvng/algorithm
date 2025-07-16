# n -> line, m -> element
def sol(A:list[list], B:list[list], n:int, m:int):
  new_matrix = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      new_matrix[i][j] = A[i][j] + B[i][j]
  return new_matrix

A = []
B = []
n, m = map(int, input().split())

for _ in range(n):
  A.append(list(map(int, input().split())))

for _ in range(n):
  B.append(list(map(int, input().split())))

for row in sol(A, B, n, m):
  print(*row)

# zip 사용
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  print(*[a + b for a,b in zip(A[i], B[i])])

