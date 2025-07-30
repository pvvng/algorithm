field = [[0] * 100 for _ in range(100)]

def sol(x, y):
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      if not field[i][j]:
        field[i][j] = 1

def count_field():
  cnt = 0
  for row in field:
    cnt += sum(row)
  return cnt

n = int(input())
for _ in range(n):
  sol(*map(int, input().split()))

print(count_field())