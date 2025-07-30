def init_dict(A:list):
  d = dict()
  d.setdefault("-", len(A))

  for a in A:
    d.setdefault(a, 0)
    d[a] += 1
  return d

def sol(d:dict, T: list):
  ans = []
  for t in T:
    ans.append(d[t]) 
  return ans

n, m = map(int, input().split())
A = input().split()

d = init_dict(A)
T = [input().strip() for _ in range(m)]

for a in sol(d, T):
  print(a)
