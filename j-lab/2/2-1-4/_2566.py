N = 9

def sol(matrix:list[list[int]]):
  maximum = -1
  row, col = -1, -1
  for i in range(N):
    for j in range(N):
      if maximum <= matrix[i][j]:
        maximum = matrix[i][j]
        row = i + 1
        col = j + 1
  return maximum, (row, col)


matrix = [list(map(int, input().split())) for _ in range(N)]
maximum, location = sol(matrix)
print(maximum)
print(*location)