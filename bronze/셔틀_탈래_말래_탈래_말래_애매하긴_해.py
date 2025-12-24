# 셔틀을 기다렸다가 타고 공학관까지 간다.
# 셔틀을 기다리지 않고 곧바로 공학관까지 걸어간다.

def sol(s, c, d):
  if s > d and c > d:
    return "T.T"
  
  if s <= d and c <= d:
    return "~.~"
  
  if s <= d and c > d:
    return "Shuttle"

  if s > d and c <= d:
    return "Walk"

a, b, c, d = map(int, input().split())
s = a + b

print(sol(s, c, d))