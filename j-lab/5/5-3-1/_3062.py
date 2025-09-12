def is_palindrome(x: str):
  start = 0; end = len(x) -1
  while start <= end:
    if x[start] != x[end]:
      return False
    start += 1
    end -= 1
  return True

def sol(N: int):
  R = list(str(N))
  R.reverse()
  R = int("".join(R))

  x = str(N + R)
  return "YES" if is_palindrome(x) else "NO"

T = int(input())
for _ in range(T):
  N = int(input())
  print(sol(N))