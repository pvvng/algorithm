def sol(matrix:list[list[int]]):
  n = 9
  maximum = -1
  row, col = -1, -1
  for i in range(n):
    for j in range(n):
      if maximum <= matrix[i][j]:
        maximum = matrix[i][j]
        row = i + 1
        col = j + 1
  return maximum, (row, col)


matrix = [list(map(int, input().split())) for _ in range(9)]
maximum, location = sol(matrix)
print(maximum)
print(*location)