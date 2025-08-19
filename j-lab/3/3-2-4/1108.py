def transform_time(t: str) -> int:
  mm, ss = map(int, t.split(":"))
  return mm * 60 + ss

def do_add_query(D:dict, start:int, end:int):
  for i in range(start, end):
    D.setdefault(i, 0)
    D[i] += 1

def do_find_query(D:dict, target:str):
  f = D.get(transform_time(target))
  return 0 if f == None else f

def sol(A: list):
  D = dict()
  ans = []
  for a in A:
    if a[0] == "1":
      start, end = transform_time(a[1]), transform_time(a[2])
      do_add_query(D, start, end)
    elif a[0] == "2":
      ans.append(do_find_query(D, a[1]))
  return ans

n = int(input())
A = [input().split() for _ in range(n)]
ans = sol(A)
for e in ans:
  print(e)