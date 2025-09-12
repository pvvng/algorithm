def sol(n: int):
  binary = ""
  while n > 0:
    binary = str(n % 2) + binary
    n //= 2

  binary = int(binary)
  ans = 0
  while binary > 0:
    ans = ans * 2 + binary % 10
    binary //= 10
  return ans
    
print(sol(int(input())))