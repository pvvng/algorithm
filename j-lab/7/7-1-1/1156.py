def fib(n: int):
  prev = ans = 1
  for _ in range(3, n + 1):
    temp = ans
    ans += prev
    prev = temp
  return ans % 987654321

n = int(input())
print(fib(n))