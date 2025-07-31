def sol(table: list, loc: tuple) -> int:
  dt = [[-1, 0], [1, 0], [0, 1], [0, -1]] # 이 방식 좋은듯

  for dx, dy in dt:
    r, c = loc[0] + dx, loc[1] + dy
    if is_range((r, c)) and table[r][c] == 1:
      return 1
  return 0

def is_range(loc: tuple):
  return 0 <= loc[0] <= 4 and 0 <= loc[1] <= 4

table = [list(map(int, input().split())) for _ in range(5)]
loc = tuple(map(int, input().split()))
print(sol(table, loc))