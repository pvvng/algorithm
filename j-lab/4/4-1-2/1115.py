# 내 풀이 (백트래킹)
def sol(n:int, current:list) -> int:
  if len(current) == n:
    return 1
  
  total = 0
  for num in range(1, 10):
    if len(current) == 0 or abs(current[-1] - num) <= 2:
      current.append(num)
      total += sol(n, current)
      current.pop()

  return total

# 재귀 x 풀이
def sol2(n: int) -> int:
  ans = 0
  for A in range(10 ** (n-1), 10**n): # n 자리수 전부 확인
    if is_ok(A):
      ans += 1
  return ans

def is_ok(A: int) -> bool:
  p = A % 10
  A //= 10
  if p == 0:
    return False
  while A > 0:
    c = A % 10 
    A //= 10
    if c == 0 or abs(p-c) > 2:
      return False
    p = c

  return True

n = int(input())
print(sol(n, []))
print(sol2(n))
