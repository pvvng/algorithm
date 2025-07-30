def solve(a: list) ->int:
  return sum(a)

def solve2(a: list) -> int:
  ans = 0
  for e in a:
    ans += e
  return ans