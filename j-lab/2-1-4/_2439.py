def sol(n: int, i: int):
  ans = ""
  for j in range(n):
    if i + j >= n - 1:
      ans += "*"
    else:
      ans += " "
  return ans

def sol2(n:int, i:int):
  return " " * (n - i - 1) + "*" * (i + 1)

n = int(input())
for i in range(n):
  print(sol(n, i))