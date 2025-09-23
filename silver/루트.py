def sol(b: int, n: int):
  root = b ** (1 / n)
  cand1, cand2 = int(root), int(root) + 1
  if abs(b - cand1 ** n) > abs(b - cand2 ** n):
    return cand2
  return cand1
  
while True:
  b, n = map(int, input().split())
  if b + n == 0:
    break
  print(sol(b, n))
