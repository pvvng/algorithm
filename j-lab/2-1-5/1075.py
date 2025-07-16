# 1. 전체 배열 순회하면서 구하기
def sol(n:int, matrix:list, i_range:tuple, j_range:tuple, k:int):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if(i_range[0] <= i <= i_range[1] and j_range[0] <= j <= j_range[1]):
        matrix[i][j] *= k
      cnt += matrix[i][j]
  return cnt


# 2. 주어진 범위만 업데이트해서 합 구하기
def sol2(matrix:list, i_range:tuple, j_range:tuple, k:int):
  for i in range(i_range[0], i_range[1]+1):
    for j in range(j_range[0], j_range[1]+1):
      matrix[i][j] *= k
  
  for row in matrix:
    cnt += sum(row)

  return cnt

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
i1, j1, i2, j2, k = map(int, input().split())
print(sol(n, matrix, (i1, i2), (j1, j2), k))
print(sol2(matrix, (i1, i2), (j1, j2), k))
