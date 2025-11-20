import sys
input = sys.stdin.readline

def memo_key(a, b, c):
  return f"{a} {b} {c}"

def w(a, b, c, memo: dict):
  n = memo.get(memo_key(a, b, c))

  if n != None:
    return n

  if a <= 0 or b <= 0 or c <= 0:
    memo.setdefault(memo_key(a, b, c), 1)
    return 1

  if a > 20 or b > 20 or c > 20:
    res = w(20, 20, 20, memo)
    memo.setdefault(memo_key(a, b, c), res)
    return res

  if a < b < c:
    res = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
    memo.setdefault(memo_key(a, b, c), res)
    return res

  res = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
  memo.setdefault(memo_key(a, b, c), res)
  return res

ans = []
memo = dict()

while True:
  a, b, c = map(int, input().split())
  if a == b == c == -1:
    break

  ret = w(a, b, c, memo)
  ans.append(f"w({a}, {b}, {c}) = {ret}")

print('\n'.join(ans))