def to_digit(n: int, k: int) -> str:
  t = ""
  while n > 0:
    t = str(n % k) + t
    n //= k
  return t

n, k = map(int, input().split())
t = to_digit(n, k)
filtered = list(filter(lambda x : x != "", t.split("0")))
sm = sum(list(map(int, filtered)))
print(to_digit(sm, k))
