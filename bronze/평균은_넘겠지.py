def sol(x: int, rest: list):
  avg = sum(rest) / x
  cnt = 0
  for e in rest:
    if e > avg:
      cnt += 1

  return "{:.3f}%".format(cnt / x * 100)

n = int(input())
for i in range(n):
  x, *rest = map(int, input().split())
  print(sol(x, rest))