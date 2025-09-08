def get_feb_day(y: int):
  if y % 4 == 0 and y % 100 != 0:
    return 29
  if y % 400 == 0:
    return 29
  return 28

def sol(y, m):
  if m == 1:
    y -= 1; m = 13
  month30 = set([4, 6, 9, 11])
  m -= 1
  if m != 2 and m in month30:
    return f"{y} {m} {30}"
  elif m == 2:
    return f"{y} {m} {get_feb_day(y)}"
  return f"{y} {m} {31}"
    
for _ in range(int(input())):
  y, m = map(int, input().split())
  print(sol(y, m))