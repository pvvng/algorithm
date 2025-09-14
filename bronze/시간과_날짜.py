def is_valid_time(x, y):
  return 0 <= x <= 23 and 0 <= y <= 59

def is_valid_month(x, y):
  day31 = set([1, 3, 5, 7, 8, 10, 12])
  day30 = set([4, 6, 9, 11])
  day29 = set([2])
  if x in day31 and 0 < y <= 31:
    return True
  if x in day30 and 0 < y <= 30:
    return True
  if x in day29 and 0 < y <= 29:
    return True
  return False

def translate(t):
  return "Yes" if t else "No"

def sol(x, y):
  return (translate(is_valid_time(x, y)), translate(is_valid_month(x, y)))

for _ in range(int(input())):
  x, y = map(int, input().split())
  print(*sol(x, y))
