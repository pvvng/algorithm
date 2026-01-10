n = int(input())
s = input()
e = s.count("e")

def sol(two, e):
  if two > e:
    return "2"
  if two < e:
    return "e"
  return "yee"

print(sol(n-e, e))
