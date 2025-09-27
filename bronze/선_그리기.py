# 1 3
# 2 5
# 4 9
# 11 13

def sol(lines: list):
  lines.sort(key=lambda x : x[0])
  ans = 0
  prev_y = -1
  for x, y in lines:
    if prev_y > x:
      x = prev_y
    if y > x:
      ans += y - x
      prev_y = y

  return ans

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
print(sol(lines))
