def sol(n, l):
  c = 0
  ans = []
  while len(ans) < n:
    c += 1
    while str(l) in str(c):
      c += 1
    ans.append(c)
  return ans[-1]

n, l = map(int, input().split())
print(sol(n, l))