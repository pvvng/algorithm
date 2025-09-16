def is_prime(a: int):
  if a < 2:
    return False

  for i in range(2, round(a ** 0.5) + 1):
    if a % i == 0:
      return False
  
  return True

def sol(A: list[int]):
  ans = 0
  for a in A:
    if is_prime(a):
      ans += 1
  return ans

n = int(input())
A = list(map(int, input().split()))
print(sol(A))