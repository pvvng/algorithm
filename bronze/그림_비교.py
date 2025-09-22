def find_diff(t1, t2):
  diff = 0
  for r in range(5):
    for c in range(7):
      if t1[r][c] != t2[r][c]:
        diff += 1
  return diff

def sol(n, P):
  mn = -1
  cand = ""
  for i in range(n):
    for j in range(i + 1, n):
      t1 = P[i]; t2 = P[j]
      diff = find_diff(t1, t2)
      if mn == -1 or diff < mn:
        mn = diff
        cand = f"{i+1} {j+1}"
  return cand

n = int(input())
P = []
for _ in range(n):
  p = []
  for _ in range(5):
    p.append(list(input()))
  P.append(p)
  
print(sol(n, P))