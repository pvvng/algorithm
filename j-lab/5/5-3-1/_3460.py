def sol(n: int):
  tr = []
  while n > 0:
    tr.append(n % 2)
    n //= 2
  ans = []
  for i in range(len(tr)):
    if tr[i] == 1:
      ans.append(str(i))
  return " ".join(ans)

T = int(input())
for _ in range(T):
  n = int(input())
  print(sol(n))
  