def sol(m:int, n:int):
  ans = []
  for t in range(m, n+1):
    is_prime = True
    for i in range(2, round(t ** 0.5) + 1):
      if t % i == 0:
        is_prime = False
        break
    if t < 2:
      is_prime = False
    if is_prime:
      ans.append(t)
  return ans

m, n = map(int, input().split())
for e in sol(m, n):
  print(e)
