import sys
input = sys.stdin.readline

def is_prime(t):
  if t < 2:
    return False
  i = 2
  while i ** 2 <= t:
    if t % i == 0:
      return False
    i += 1
  return True

def sol(m, n):
  ans = []
  for t in range(m, n + 1):
    if is_prime(t):
      ans.append(t)
  if len(ans) == 0:
    print(-1)
  else:
    print(sum(ans))
    print(ans[0])

m, n = [int(input()) for _ in range(2)]
sol(m, n)
