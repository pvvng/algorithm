def get_nums():
  d = dict()
  for i in range(26):
    d.setdefault(i + 10, chr(ord("A") + i))
  for i in range(10):
    d.setdefault(i, str(i))
  return d

def sol(N, B):
  ans = ""
  tr = get_nums()
  while N > 0:
    ans = tr[(N % B)] + ans
    N //= B
  return ans

N, B = map(int, input().split())
print(sol(N, B))
