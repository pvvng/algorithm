def is_prime(a: int):
  if a < 2:
    return False

  i = 2
  while i * i <= a:
    if a % i == 0:
      return False
    i += 1

  return True
 
def sol(A: list):
  ans = 0
  for a in A:
    if is_prime(a):
      ans += a
  return ans

A = list(map(int, input().split()))
print(sol(A))