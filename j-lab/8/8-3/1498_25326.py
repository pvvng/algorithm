import sys
input = sys.stdin.readline

def sol(T, Q):
  ans = []
  for q in Q:
    res = 0
    for t in T:
      if is_ok(q, t):
        res += 1
    ans.append(str(res))
  return ans

def is_ok(q, t):
  for i in range(3):
    if q[i] != "-" and q[i] != t[i]:
      return False
  return True

n, m = map(int, input().split())
T = [input().split() for _ in range(n)]
Q = [input().split() for _ in range(m)]
print("\n".join(sol(T, Q)))