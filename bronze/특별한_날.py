mm = int(input())
dd = int(input())

def sol(mm, dd):
  if mm < 2:
    return "Before"
  if mm == 2:
    if dd == 18:
      return "Special"
    if dd < 18:
      return "Before"
  return "After"

print(sol(mm, dd))