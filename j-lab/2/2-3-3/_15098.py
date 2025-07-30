def sol(t:list):
  s = set()
  for e in t:
    if e in s:
      return "no"
    s.add(e)
  return "yes"

t = input().split()
print(sol(t))