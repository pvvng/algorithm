def reverse(t:str):
  return t[::-1]

def sol(a:str, b:str):
  a, b = int(reverse(a)), int(reverse(b))
  return a if a > b else b

a, b = map(str, input().split())
print(sol(a, b))